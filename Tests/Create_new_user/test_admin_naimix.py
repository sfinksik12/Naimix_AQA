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
def test_create_user(desktop_auth_admin_naimix, lastname, name, sername, position, role, phone, email, password, repeatPassword):
    app = desktop_auth_admin_naimix

    app.main_page.open_naimix_settings()
    app.naimix_settings_page.open_employees_tab()
    app.naimix_settings_page.click_create_employee()
    app.create_user_page.fill_fields(lastname, name, sername, position, role, phone, email, password, repeatPassword)
    app.create_user_page.click_add_user()


