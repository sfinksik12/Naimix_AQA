from Data import users


def test_Admin_Naimix_Create_Company(desktop_api):
    desktop_api.POST(
        'https://nm-test.mmtr.ru/api/clients/add',
        users.Admin_Naimix['auth_token'],
        data=users.payload

    )


def test_Admin_Naimix_filter(desktop_api):
    desktop_api.POST(
        'https://nm-test.mmtr.ru/api/clients/users/getPage',
        users.Admin_Naimix['auth_token'],
        data=users.titi
    )
