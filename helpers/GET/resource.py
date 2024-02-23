import requests


class Resource:
    def __init__(self):
        requests.get('https://reqres.in/api/{resource}', params={'resource': ''})
