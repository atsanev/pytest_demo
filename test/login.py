import pytest

from helpers.POST.login import *
from fixtures.users import *

@pytest.mark.parametrize("user", [userOne, userTwo])
def test_login(user):
    token = login()
    assert token