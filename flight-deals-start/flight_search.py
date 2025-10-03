import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,amad_api:str,amad_api_secret:str):
        self.api = amad_api
        self.api_secret = amad_api_secret
        self.secret = amad_api_secret
        self.token = self.get_token()
        self.headers = {
                "Authorization": f'Bearer {self.token}',
                "Accept": "application/vnd.amadeus+json"
            }

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
        return token

    # return a dict of city:iataCode
    def get_iatas(self,city_lst:list) -> dict:
        '''Takes a list of cities and returns a list of iataCodes'''
        result = []
        for city in city_lst:
            url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
            parameters = {
                "keyword":city,
                "max": 1
            }
            response = requests.get(url=url,params=parameters, headers=self.headers)
            if response.status_code == 200:
                result.append(response.json()['data'][0]['iataCode'])
            else:
                return response.json()
        return result
    
    def get_lower_prices(self,iata_code:str,date:str):
        url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        body={
            "currencyCode": "GBP",
            "originDestinations": [
                {
                "id": "1",
                "originLocationCode": "LON",
                "destinationLocationCode": iata_code,
                "departureDateTimeRange": {
                    "date": date
                }
                }
            ],
            "travelers": [
                {
                "id": "1",
                "travelerType": "ADULT"
                }
            ]
        }


        response = requests.post(url=url,json=body,headers=self.headers)
        print(response.json())




