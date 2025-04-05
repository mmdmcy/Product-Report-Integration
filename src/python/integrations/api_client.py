class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def fetch_data(self, endpoint):
        import requests
        
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def post_data(self, endpoint, data):
        import requests
        
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()