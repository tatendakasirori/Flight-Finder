import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,amad_api,amad_api_secret):
        self.api = amad_api
        self.api_secret = amad_api_secret
        self.secret = amad_api_secret
    

    def get_token(self) -> str:
        '''Returns your latest amadeus token'''
        
        url = "https://test.api.amadeus.com/v1/security/oauth2/token" 
        headers = {'Content-Type': 'application/x-www-form-urlencoded'} 
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.api,
            'client_secret': self.api_secret
        }
        response = requests.post(url=url,data=data, headers=headers)
        token = response.json()['access_token']
        self.token = token

    # return a dict of city:iataCode
    def get_iatas(self,city_lst) -> dict:
        '''Takes a list of cities and returns a dict of city:iataCode'''
        for city in city_lst:
            