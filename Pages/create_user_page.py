from playwright.sync_api import Page
from Locators import elements_create_user_form
import time


class CreateUserForm():
    def __init__(self, page: Page):
        self.page = page

    def choose_drop_down_element(self, title: str):
        self.page.query_selector(f'div.nm-dropdown-v2__item-content[title="{title}"]').click()

    def fill_fields(self):
        self.page.fill(elements_create_user_form.LASTNAME, 'Щелоков')
        self.page.fill(elements_create_user_form.NAME, 'Павел')
        self.page.fill(elements_create_user_form.SERNAME, 'Михайлович')
        self.page.click(elements_create_user_form.POSITION)
        self.choose_drop_down_element('Менеджер')
        time.sleep(2)

