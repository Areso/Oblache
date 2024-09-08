import locust


def check_http_response(response):
    if response.status_code != 200:
        response.failure(f'Incorrect status code {response.status_code}')


