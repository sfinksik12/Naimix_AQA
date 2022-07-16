import settings
from Data import users
from pytest import fixture
from Pages.application import App
from playwright.sync_api import sync_playwright


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def desktop(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL)
    app.goto('')
    yield app
    app.close()
