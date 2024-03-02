from .common import BeautifulSoup, requests
from . import head, env


class Auth:
    def __init__(self):
        self.username = env["USERNAME"]
        self.password = env["PASSWORD"]
        self.s = requests.session()

    def login(self):
        login_url = f"{env['BASE_URL']}/{env['LOGIN_URL']}"
        data = {
            "txt_username": self.username,
            "txt_password": self.password
        }
        return self.s.post(login_url, data=data, headers=head)

    def get_login(self):
        dashboard_url = f"{env['BASE_URL']}/{env['DASHBOARD_URL']}"
        response = self.s.get(dashboard_url, headers=head)
        soup = BeautifulSoup(response.content, "html.parser")
        link_element = soup.find("a", href=lambda href: href.startswith("../sipandai/?mod=login&act=loginact&id="))
        link_href = link_element["href"]
        cleaned_link = link_href.replace("../sipandai/", "")
        login_url = f"{env['BASE_URL2']}/{cleaned_link}"
        return self.s.get(login_url, headers=head)
    
    def login_(self):
        url = input("url >> ")
        return self.s.get(url, headers=head)

    def logout(self):
        logout_url = f"{env['BASE_URL2']}/{env['LOGOUT_URL']}"
        response = self.s.get(logout_url, headers=head)
        if response.status_code == 200:
            return True