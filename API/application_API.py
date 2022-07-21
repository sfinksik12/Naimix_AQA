from playwright.sync_api import Playwright


class App_Api:
    def __init__(self, playwright: Playwright):
        self.api_context = playwright.request.new_context()

    def GET(self, endpoint):
        response = self.api_context.get(endpoint)
        assert response.status == 200

    def POST(self, endpoint, api_token, data):
        response = self.api_context.post(
            endpoint,
            headers={
                "Accept": "application/json;charset=UTF-8",
                'Authorization': f'Bearer {api_token}',
                'Content-Type': 'application/json'
                },
            data=data,
        )
        print(response.text)



