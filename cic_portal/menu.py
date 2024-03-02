from .common import BeautifulSoup, dn, re
from . import head, env


class Menu:
    def __init__(self, auth):
        self.auth = auth
        self.no_list = []
        self.subject_list = []
        self.links_list = []
        self.selected_matkul = None 

    def class_list(self):
        matk = self.auth.s.get(f"{env['BASE_URL2']}/{env['MATKUL_URL']}", headers=head)
        soup = BeautifulSoup(matk.content, "html.parser")
        class_table_header = soup.find(lambda tag: tag.name == "h4" and tag.string.startswith("Daftar Kelas Yang Diikuti"))
        whoami_header = soup.find(lambda tag: tag.name == "h4" and tag.string.startswith("JADWAL KULIAH"))
        if class_table_header:
            whoami_table = whoami_header.find_next("table")
            whoami_tr = whoami_table.find_all("tr")
            print(whoami_tr[2].find("b").get_text())
            kelas_table = class_table_header.find_next("table")
            rows = kelas_table.find_all("tr")
            for row in rows[1:]:  
                cells = row.find_all("td")
                no = cells[0].text.strip()
                subject = cells[2].text.strip()
                link = cells[4].find("a")["href"] if cells[4].find("a") else "No link available"
                self.no_list.append(no)
                self.subject_list.append(subject)
                self.links_list.append(link)
            for no, subject, link in zip(self.no_list, self.subject_list, self.links_list):
                part = subject.split()
                link = link.split("course_id=")[1]
                result = " ".join(part[1:])
                print(f"{no} {result} ({link})")
    
    def meeting_list(self):
        selected_no = input("Pilih No. Mata Kuliah: ")
        try:
            selected_no = int(selected_no)
            if 1 <= selected_no <= len(self.no_list):
                selected_link = self.links_list[selected_no - 1]
                self.selected_matkul = f"{env['BASE_URL2']}/{selected_link}"
                get = self.auth.s.get(self.selected_matkul, headers=head)
                soup = BeautifulSoup(get.content, "html.parser")
                class_table = soup.find_all("table", class_="table table-hover table-striped")
                if class_table:
                    class_table = class_table[1]
                    rows = class_table.find_all("tr")
                    meetings_info = {}
                    print("------------------------------")
                    for idx, row in enumerate(rows, 1):
                        date_pattern = re.compile(r"(Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu), \d{2} (Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember) \d{4}, Jam : \d{2}:\d{2}")
                        date_elements = row.find_all(string=date_pattern)
                        for date in date_elements:
                            date = re.sub(r'[\n\t\s]+', ' ', date_elements[0]).strip().split(", Jam")[0]
                            pertemuan_element = row.find("h6")
                            meeting_tittle = pertemuan_element.text.split(" Pokok Bahasan :")[0] if pertemuan_element else "N/A"
                            join_link_element = row.find("a", class_="btn app-btn-primary", href=True)
                            join_link_info = join_link_element["href"] if join_link_element else "No link available"
                            discuss_id = None
                            course_id = None
                            if "id=" in join_link_info and "courses_id=" in join_link_info:
                                discuss_id = join_link_info.split("id=")[1].split("&")[0]
                                course_id = join_link_info.split("courses_id=")[1].split("&")[0]
                            meetings_info[idx] = {
                                "meeting_tittle": meeting_tittle,
                                "discuss_id": discuss_id,
                                "course_id": course_id
                            }
                            meeting_tittle = re.sub(r"Materi Perkuliahan | :", "", meeting_tittle)

                            print(f"{idx}. ({discuss_id}) {meeting_tittle} {'(today)' if date == dn() else ''}")
                            print("------------------------------")
                    return meetings_info
            else:
                print("Invalid selection.")
                return False
        except ValueError:
            print("Invalid input.")
            return False

        
    def presence_display(self):
        if self.selected_matkul is None:
            return
        response = self.auth.s.get(self.selected_matkul, headers=head)
        soup = BeautifulSoup(response.content, "html.parser")
        class_table = soup.find_all("table", class_='table table-bordered')
        absen = class_table[0]
        td_nbuttons = absen.find_all("td")
        presence = ""
        for i, td_element in enumerate(td_nbuttons, start=1):
            button = td_element.find("button")
            if button: 
                title = button.get("title", "Tidak ada atribut title").strip()
                presence += f"{i} Hadir {title}\n"
            else:
                presence += f"{i} Tidak Hadir\n"
        print('-------------- Daftar Kehadiran -------------')
        print(presence)
            