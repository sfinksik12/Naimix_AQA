from playwright.sync_api import Playwright
from Locators import elements_login_page
from .main_app_page import MainPage
from .Naimix_Settings_Page import NaimixSettingsPage
from .create_user_page import CreateUserForm


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.headless = headless
        self.base_url = base_url
        self.browser = playwright.chromium.launch(headless=False, )
        self.context = self.browser.new_context(locale='ru_RU')
        self.page = self.context.new_page()
        self.api_request_context = self.context.request
        #!!!
        self.api_context = playwright.request.new_context()



        # Pages
        self.Main_Page = MainPage(self.page)
        self.Naimix_Settings_Page = NaimixSettingsPage(self.page)
        self.Create_User_Page = CreateUserForm(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def login(self, data: dict):
        self.page.fill(elements_login_page.LOGIN_FIELD, data['login'])
        self.page.fill(elements_login_page.PASSWORD_FIELD, data['password'])
        self.page.locator(elements_login_page.ENTER_BTN).click()

    def GET(self, endpoint):
        response = self.api_context.get(endpoint)
        return response


    def POST(self, endpoint, api_token, data):
        self.response = self.api_request_context.post(
            endpoint,
            headers={
                "Accept": "application/json;charset=UTF-8",
                'Authorization': f'Bearer {api_token}',
                'Content-Type': 'application/json'
                },
            data=data,
        )
        print(self.response.json())
        return self.response.json()

