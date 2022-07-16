import settings
from pytest import fixture
from Pages.application import App
from playwright.sync_api import sync_playwright


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def desktop(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL)
    app.goto('')
    yield app
    app.close()
