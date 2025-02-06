from pytest_demo import session
from fixtures.users import *

def login():
    baseUrl = baseUrl
    username = userOne['username']
    password = userOne['password']

    token = APIClient(baseUrl, username, password)
    return token

