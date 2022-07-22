import json

from Data import users


def test_one(desktop_api):
    desktop_api.POST(
        '/clients/users/getPage',
        users.Admin_Naimix,
        users.q
    )
