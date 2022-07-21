import settings
from Data import users
from pytest import fixture
from Pages.application import App
from API.application_API import App_Api
from playwright.sync_api import sync_playwright


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def desktop(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL)
    yield app
    app.close()

@fixture
def desktop_api(get_playwright):
    app = App_Api(get_playwright)
    yield app


@fixture()
def desktop_auth_admin_naimix(desktop):
    desktop.goto('')
    desktop.login(users.Admin_Naimix)
    yield desktop


@fixture()
def desktop_auth_manager_naimix(desktop):
    desktop.goto('')
    desktop.login(users.Manager_Naimix)
    yield desktop


