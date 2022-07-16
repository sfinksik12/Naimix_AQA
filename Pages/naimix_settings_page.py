from playwright.sync_api import Page
from Locators import elements_settings_of_naimix_page


class NaimixSettingsPage():
    def __init__(self, page: Page):
        self.page = page

    def open_employees_tab(self):
        self.page.click(elements_settings_of_naimix_page.EMPLOYEES)

    def click_create_employee(self):
        self.page.click(elements_settings_of_naimix_page.CREATE_NEW_EMPLOYEE_BTN)



