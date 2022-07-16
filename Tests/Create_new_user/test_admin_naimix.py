from Data import users
from pytest import mark

data = [('Ваганов', 'Павел', 'Михайлович',
         'Менеджер', 'Администратор Наймикс',
         '9536447612', 'www@list.ru',
         'Www1234!', 'Www1234!'
         )]


@mark.parametrize('lastname, name, sername,'
                  'position, role, '
                  'phone, email, '
                  'password, repeatPassword', data)
def test_create_user(desktop, lastname, name, sername, position, role, phone, email, password, repeatPassword):
    desktop.login_as(users.Admin_Naimix)
    desktop.main_page.open_naimix_settings()
    desktop.naimix_settings_page.open_employees_tab()
    desktop.naimix_settings_page.click_create_employee()
    desktop.create_user_page.fill_fields(lastname, name, sername, position, role, phone, email, password, repeatPassword)
    desktop.create_user_page.click_add_user()
