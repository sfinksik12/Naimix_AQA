import Settings
from Data import Users
from pytest import fixture
from Pages.application import App
from API.Application_API import App_Api
from playwright.sync_api import sync_playwright


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def desktop(get_playwright):
    app = App(get_playwright, base_url=Settings.BASE_URL_UI)
    yield app
    app.close()


# API
@fixture
def desktop_api():
    api = App_Api(Settings.BASE_URL_API)
    yield api
    api.close()


# Authorization roles in UI
@fixture()
def desktop_auth_admin_naimix(desktop):
    desktop.goto('')
    desktop.login(Users.Admin_Naimix)
    yield desktop


@fixture()
def desktop_auth_manager_naimix(desktop):
    desktop.goto('')
    desktop.login(Users.Manager_Naimix)
    yield desktop


