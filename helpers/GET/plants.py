from session import APIClient
from fixtures.url import baseUrl

def get_plants(token):
    client = APIClient(baseUrl, token=token)
    response = client.get_data('plants')
    return response

