import pytest

from helpers.POST.login import *
from fixtures.users import *

def test_login():
    token = login(userOne['username'], userOne['password'])
    assert token is not None

def test_login_invalid_credentials():
    with pytest.raises(Exception) as exc_info:
        login(userOne['username'], "invalid_password")
    assert "Login failed" in str(exc_info.value)

def test_login_empty_credentials():
    with pytest.raises(Exception) as exc_info:
        login("", "")
    assert "Login failed" in str(exc_info.value)

def test_login_invalid_email():
    with pytest.raises(Exception) as exc_info:
        login("invalid_email", userOne['password'])
    assert "Login failed" in str(exc_info.value)

def test_login_invalid_password():
    with pytest.raises(Exception) as exc_info:
        login(userOne['username'], "invalid_password")
    assert "Login failed" in str(exc_info.value)

def test_login_empty_email():
    with pytest.raises(Exception) as exc_info:
        login("", userOne['password'])
    assert "Login failed" in str(exc_info.value)

def test_login_empty_password():
    with pytest.raises(Exception) as exc_info:
        login(userOne['username'], "")
    assert "Login failed" in str(exc_info.value)

def test_login_invalid_email_format():
    with pytest.raises(Exception) as exc_info:
        login("invalid_email_format", userOne['password'])
    assert "Login failed" in str(exc_info.value)
