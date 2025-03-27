import requests

class APIClient:
    def __init__(self, base_url, username=None, password=None, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        if username and password:
            self.token = self.authenticate(username, password)
        elif token:
            self.token = token
        else:
            raise ValueError("Either username/password or token must be provided")

    def authenticate(self, username, password):
        login_url = f"{self.base_url}/login"
        credentials = {'username': username, 'password': password}
        response = self.session.post(login_url, json=credentials)
        if response.status_code == 200:
            token = response.json().get('token')
            if token:
                print('Login Successful')
                return token
            else:
                raise Exception("Token not found in login response")
        else:
            raise Exception(f"Login failed: {response.status_code} {response.text}")

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f"Bearer {self.token}"
        }

    def get_data(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")
    
    def post_data(self, endpoint, data, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data, headers=self.get_headers())
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create data: {response.status_code} {response.text}")

    def delete_data(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, headers=self.get_headers())
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Failed to delete data: {response.status_code} {response.text}")

    def patch_data(self, endpoint, data, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.patch(url, json=data, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to patch data: {response.status_code} {response.text}")
