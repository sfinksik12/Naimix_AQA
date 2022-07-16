from Data import users
import time

def test_create_company(desktop):
    desktop.login_as(users.Admin_Naimix)
    desktop.main_page.open_naimix_settings()
    desktop.naimix_settings_page.open_employees_tab()
    desktop.naimix_settings_page.click_create_employee()
    desktop.create_user_page.fill_fields()

