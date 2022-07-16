from playwright.sync_api import Page
from Locators import element_create_user_form


class CreateUserForm:
    def __init__(self, page: Page):
        self.page = page

    # REFACTOR
    def choose_drop_down_element(self, title: str):
        self.page.query_selector(f'div.nm-dropdown-v2__item-content[title="{title}"]').click()

    def fill_fields(self, lastname, name, sername, position, role, phone, email, password, repeatPassword):
        self.page.fill(element_create_user_form.LASTNAME, lastname)
        self.page.fill(element_create_user_form.NAME, name)
        self.page.fill(element_create_user_form.SERNAME, sername)

        self.page.click(element_create_user_form.POSITION)
        self.choose_drop_down_element(position)

        self.page.click(element_create_user_form.ROLE)
        self.choose_drop_down_element(role)

        self.page.fill(element_create_user_form.PHONE, phone)
        self.page.fill(element_create_user_form.EMAIL, email)

        self.page.fill(element_create_user_form.PASSWORD, password)
        self.page.fill(element_create_user_form.REPEAT_PASSWORD, repeatPassword)

    def click_add_user(self):
        self.page.click(element_create_user_form.ADD)
