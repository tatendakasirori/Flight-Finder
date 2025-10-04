import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

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
    
    def get_lower_prices(self,iata_code:str):
        tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        six_months = (datetime.today() + timedelta(days=6)).strftime('%Y-%m-%d')
        url = 'https://test.api.amadeus.com/v1/shopping/flight-offers'
        body={
            'origin':iatacode,
            'destination':iata_code,
            'departureDate':thnga, #string (query) the date, or range of dates, on which the flight will depart from the origin. Dates are specified in the ISO 8601 YYYY-MM-DD format, e.g. 2017-12-25. Ranges are specified with a comma and are inclusive
            'maxPrice':300,
            
        }

        response = requests.post(url=url,json=body,headers=self.headers)
        print(response.json())




