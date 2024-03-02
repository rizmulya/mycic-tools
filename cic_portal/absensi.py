from .common import BeautifulSoup, hashlib, sys
from . import head, env


class Absensi():
    def __init__(self, auth):
        self.auth = auth

    def exec(self, meeting_data):
        if meeting_data is False:
            return
        try:
            selected_pertemuan = int(input("Pilih nomor pertemuan: "))
            if selected_pertemuan in meeting_data:
                selected_data = meeting_data[selected_pertemuan]
                discuss_id = selected_data["discuss_id"]
                course_id = selected_data["course_id"]
                val = f"{env['BASE_URL2']}/?mod=sipandai&act=discuss&id={discuss_id}&courses_id={course_id}"
                absen_url = f"{env['BASE_URL2']}/?mod=sipandai&act=discussabsen&id={discuss_id}&courses_id={course_id}"
                print("Anda memilih:", selected_data["meeting_tittle"])
                req = self.auth.s.get(val, headers=head)
                pert = BeautifulSoup(req.content, "html.parser")
                but = pert.find('a', href=lambda href: href and href.startswith("views/validasi/index.php?mod="))
                if not but:
                    print("Waktu absen berakhir\nlogging out")
                    self.auth.s.get(f"{env['BASE_URL2']}/{env['LOGOUT_URL']}", headers=head)
                    sys.exit()
                datum = {"qrcode": f"{hashlib.md5(hashlib.md5(discuss_id.encode()).hexdigest().encode()).hexdigest()}"}
                r_post = self.auth.s.post(absen_url, data=datum, headers=head)
                self.__display(r_post)
                return True
            else:
                print("Invalid selection.")
                return False
        except ValueError:
            print("Invalid input.")
            return False
        
    def manual(self, course_id, discuss_id):
        absen_url = f"{env['BASE_URL2']}/?mod=sipandai&act=discussabsen&id={discuss_id}&courses_id={course_id}"
        datum = {"qrcode": f"{hashlib.md5(hashlib.md5(discuss_id.encode()).hexdigest().encode()).hexdigest()}"}
        try:
            response = self.auth.s.post(absen_url, data=datum, headers=head)
            self.__display(response)
            return True
        except:
            pass
            
    def __display(self, response):
        soup_post = BeautifulSoup(response.content, "html.parser")
        if response.status_code == 200:
            card = soup_post.find_all("div", class_="card")
            card = card[2]
            print(card.prettify())
        