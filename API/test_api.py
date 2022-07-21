from playwright.sync_api import APIRequestContext
from Base.test_apis_file import api_request_context


def test_should_create_bug_report(api_request_context: APIRequestContext) -> None:
    data = {"login": "nmadmin", "password": "nmadmin123"}
    new_issue = api_request_context.post('https://nm-test.mmtr.ru/api/auth/login', data=data)
    assert new_issue.ok

