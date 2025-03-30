import pytest
from helpers.POST.plants import post_plants
from helpers.POST.login import login
from fixtures.users import userOne
from fixtures.plants import *

def get_token():
    token = login(userOne['username'], userOne['password'])
    return token

def test_create_plants():
    token = get_token()
    response = post_plants(token, duplicateRubberPlant)
    assert response.status_code == 201
    assert response.json()['message'] == 'Plant created successfully'


