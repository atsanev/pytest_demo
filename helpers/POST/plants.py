from session import APIClient
from fixtures.url import baseUrl

def post_plants(token, data):
    client = APIClient(baseUrl, token=token)
    response = client.post_data('plants', data)
    return response

