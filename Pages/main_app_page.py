from playwright.sync_api import Page
from Locators import elements_main_page


class MainPage():
    def __init__(self, page: Page):
        self.page = page

    def open_naimix_settings(self):
        self.page.click(elements_main_page.SETTINGS)

    def create_company(self):
        self.page.click(elements_main_page.CREATE_COMPANY_BTN)




