from .common import BeautifulSoup, to_csv, to_img
from . import head, env


class Extractor:
    def __init__(self, auth):
        self.auth = auth

    def attendance(self):
        res = self.auth.s.get(f"{env['BASE_URL']}/{env['COURSE_URL']}", headers=head)
        soup = BeautifulSoup(res.content, "html.parser")
        table = soup.find_all('table', class_='table table-hover table-striped')
        table = table[1]
        data = []
        rows = table.find_all('tr')[1:]  
        for row in rows:
            columns = row.find_all('td')
            no = columns[0].text.strip().rstrip('.')
            day_time = ' '.join(columns[1].text.split()).strip()
            class_room = ' '.join(columns[2].text.split()).strip()
            subject = ' '.join(columns[3].text.split()[1:]).strip()
            lecture = columns[4].text.strip()

            data.append({
                'No': no,
                'Hari & Waktu': day_time,
                'Kelas & Ruangan': class_room,
                'Mata Kuliah': subject,
                'Dosen Pengampuh': lecture
            })

        to_csv(data, "Reports/jadwal.csv")
        # to_img("Reports/jadwal.csv", "Reports/jadwal.png")
        return True