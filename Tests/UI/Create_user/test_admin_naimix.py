from pytest import mark

data = [
    ('Ваганов', 'Павел', 'Михайлович',
     'Менеджер', 'Администратор Наймикс',
     '9536447612', 'qqqwe@list.ru',
     'Www1234!', 'Www1234!'
     ),

    ('Петров', 'Павел', 'Михайлович',
     'Менеджер', 'Администратор Наймикс',
     '9536447612', 'weq@list.ru',
     'Www1234!', 'Www1234!'
     )
]


@mark.parametrize('lastname, name, sername,'
                  'position, role, '
                  'phone, email, '
                  'password, repeatPassword', data)
def test_create_user(desktop_auth_admin_naimix, lastname, name, sername, position, role, phone, email, password,repeatPassword):
    app = desktop_auth_admin_naimix

    app.Main_Page.open_naimix_settings()
    app.Naimix_Settings_Page.open_employees_tab()
    app.Naimix_Settings_Page.click_create_employee()
    app.Create_User_Page.fill_fields(lastname, name, sername, position, role, phone, email, password, repeatPassword)
    app.Create_User_Page.click_add_user()
