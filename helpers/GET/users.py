import requests


class Users:
    def __init__(self, session):
        self.session = session
        self.__users_path = 'https://reqres.in/api/users'

    def get_users(self):
        self.session.get(self.__users_path)
        assert self.session.response.status_code == 200
