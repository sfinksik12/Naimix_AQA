from playwright.sync_api import Playwright
from Locators import elements_login_page
from .main_app_page import MainPage
from .naimix_settings_page import NaimixSettingsPage
from .create_user_page import CreateUserForm


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.headless = headless
        self.base_url = base_url
        self.browser = playwright.chromium.launch(headless=False, )
        self.context = self.browser.new_context(locale='ru_RU')
        self.page = self.context.new_page()

        # Pages
        self.main_page = MainPage(self.page)
        self.naimix_settings_page = NaimixSettingsPage(self.page)
        self.create_user_page = CreateUserForm(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.browser.close()
        self.browser.close()

    def login_as(self, data: list):
        self.page.fill(elements_login_page.LOGIN_FIELD, data[0])
        self.page.fill(elements_login_page.PASSWORD_FIELD, data[1])
        self.page.locator(elements_login_page.ENTER_BTN).click()
