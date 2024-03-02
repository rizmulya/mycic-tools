from cic_portal.utils.parser import parser
from cic_portal.auth import Auth
from cic_portal.menu import Menu
from cic_portal.absensi import Absensi
from cic_portal.extractor import Extractor


def main(args, auth, menu):
    if args.absen and args.manual:
        course_id = input(">> course_id: ")
        discuss_id = input(">> discuss_id: ")
        absensi = Absensi(auth)
        if absensi.manual(course_id, discuss_id):
            menu.presence_display()
    elif args.absen:
        menu.class_list()
        meeting_info = menu.meeting_list()
        absensi = Absensi(auth)
        if absensi.exec(meeting_info):
            menu.presence_display()
    elif args.jadwal:
        extractor = Extractor(auth)
        extractor.attendance()


def authenticate(args):
    auth = Auth()
    response = auth.login()
    if "Session Loading" in response.text:
        menu = Menu(auth)
        main(args, auth, menu)
        if auth.logout():
            print("\nlogging out")
    else:
        print("Username atau Password salah.")


if __name__ == "__main__":
    args = parser()
    if args:
        authenticate(args)
