from Data import users


def test_create_company(desktop):
    desktop.login_as(users.Admin_Naimix)
    desktop.main_page.create_company()


