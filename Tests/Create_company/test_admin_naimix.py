import time

def test_admin(desktop_auth_admin_naimix):
    desktop_auth_admin_naimix.main_page.create_company()
    time.sleep(2)

def test_maneger(desktop_auth_manager_naimix):
    desktop_auth_manager_naimix.main_page.create_company()
    time.sleep(2)