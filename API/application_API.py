import requests
import settings


class App_Api:
    def __init__(self, base_url: str):
        self.session = requests.session()
        self.base_url = base_url

    def Status_Code_is_200(self):
        request = self.session.get(self.base_url)
        assert request.status_code == 200

    def Get_Bearer_Token(self, auth: dict):
        request = self.session.post(
            url=self.base_url + '/auth/login',
            data=auth,
            headers=settings.HEADERS
        )
        return request.json()['accessToken']

    def POST(self, endpoint: str, auth: dict, data: dict):
        token = self.Get_Bearer_Token(auth)
        request = self.session.post(
            url=self.base_url + endpoint,
            data=data,
            headers=
            {
                "Accept": "application/json;charset=UTF-8",
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            },
        )

    def close(self):
        self.session.close()
