import json

from Data import Users


def test_one(desktop_api):
    desktop_api.Post(
        '/clients/users/getPage',
        Users.Admin_Naimix,
        Users.example
    )
