from helpers.GET.users import *

session = requests.Session()
users = Users(session)

"this will not work because there's no session yet need to create a new session and controller"
def test_get_users():
    response = users.get_users()
    response.json()
    assert response.status_code == 200
