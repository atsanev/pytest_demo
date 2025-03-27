from session import APIClient
from fixtures.users import userOne
from fixtures.url import baseUrl

def login(username=None, password=None):
    if username is None:
        username = userOne['username']
    if password is None:
        password = userOne['password']

    token = APIClient(baseUrl, username, password)
    return token

