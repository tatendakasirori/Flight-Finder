import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,url,auth):
        self.url = url
        self.auth = auth
        self.headers = sh_headers={
        'Authorization': auth,
        "Content-Type": "application/json"
        }

    # gets a list of all cities in the sheet
    def get_cities(self):
        response = requests.get(url=self.url,headers=self.headers)
        prices = response.json()['prices']
        city_list = [i['city'] for i in prices]
        return city_list





