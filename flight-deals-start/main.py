#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from dotenv import load_dotenv
import os
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()

#sheety object for handling google sheet data
sheety_data = DataManager(url=os.getenv("SH_URL"),auth=os.getenv("SH_AUTH"))

#get the list of cities in the google sheet
list = sheety_data.get_cities()

#FlightSearch object for talking to the flight search api
flights = FlightSearch(amad_api=os.getenv("AMAD_API"), amad_api_secret=os.getenv("AMAD_API_SECRET"))

#get iatacodes for the cities in list using the FlightSearch object
iatacodes = flights.get_iatas(list)

#enter the iatacodes into the google sheets
sheety_data.write_iata(iatacodes)

