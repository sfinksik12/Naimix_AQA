from Data import users


def test_Admin_Naimix_login(desktop):
    desktop.POST(
        'https://nm-test.mmtr.ru/api/clients/add',
        users.Admin_Naimix['auth_token'],
        data=users.payload
    )
