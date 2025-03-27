import pytest
from helpers.GET.plants import get_plants
from helpers.POST.login import login
from fixtures.users import userOne


def get_token():
    token = login(userOne['username'], userOne['password'])
    return token

def test_get_plants():
    login = get_token()
    response = get_plants(login)
    assert response is not None
    assert 'id' in response[0]
    assert 'name' in response[0]
    assert 'species' in response[0]
    assert 'light' in response[0]
    assert 'water' in response[0]
    assert 'humidity' in response[0]
    assert 'toxicity' in response[0]
    assert len(response) > 0


def test_get_plants_invalid_token():
    with pytest.raises(Exception) as exc_info:
        response = get_plants("invalid_token")
        assert response.status_code == 403
    assert "Forbidden" in str(exc_info.value)

def test_get_plants_empty_token():
    with pytest.raises(Exception) as exc_info:
        get_plants("")
    assert "Either username/password or token must be provided" in str(exc_info.value)

def test_get_plants_no_token():
    with pytest.raises(Exception) as exc_info:
        response = get_plants(None)
        assert response.status_code == 403
    assert "Either username/password or token must be provided" in str(exc_info.value)

def test_get_plants_invalid_token_format():
    with pytest.raises(Exception) as exc_info:
        response = get_plants("invalid_token_format")
        assert response.status_code == 403
    assert "Failed to fetch data: 403 Forbidden" in str(exc_info.value)

def test_get_plants_invalid_token_type():
    with pytest.raises(Exception) as exc_info:
        response = get_plants(123)
        assert response.status_code == 403
    assert "Failed to fetch data: 403 Forbidden" in str(exc_info.value)






















