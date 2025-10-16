#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from dotenv import load_dotenv
import os
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime,timedelta
from flight_data import FlightData
from notification_manager import NotificationManager

load_dotenv()
'''U should make main in such a way that i only puts the iatacodes once and thats it'''

# #sheety object for handling google sheet data
# sheety_data = DataManager(url=os.getenv("SH_URL"),auth=os.getenv("SH_AUTH"))

# #get the list of cities in the google sheet
# list = sheety_data.get_cities()

#FlightSearch object for talking to the flight search api
#flights = FlightSearch(amad_api=os.getenv("AMAD_API"), amad_api_secret=os.getenv("AMAD_API_SECRET"))

# #get iatacodes for the cities in list using the FlightSearch object
# iatacodes = flights.get_iatas(list)

# #enter the iatacodes into the google sheets
# sheety_data.write_iata(iatacodes)

###########ALGORITHM##########
''' Flight_search.get_flights(list of iatacodes) -> FlightData.filter_by_price(flights from Flight_search)'''

test_citydata_dict = {
    'Paris': ['PAR', 90], 
    'Frankfurt': ['FRA', 110], 
    'Tokyo': ['TYO', 585], 
    'Hong Kong': ['HKG', 551], 
    'Istanbul': ['IST', 130], 
    'Kuala Lumpur': ['KUL', 614], 
    'New York': ['NYC', 360], 
    'San Francisco': ['SFO', 360], 
    'Dublin': ['DBN', 378]
    }

flight_data = FlightData(citydata_dict=test_citydata_dict)

flights_search = FlightSearch(amad_api=os.getenv("AMAD_API"), amad_api_secret=os.getenv("AMAD_API_SECRET"))

flights = flights_search.get_flights(['PAR', 'FRA', 'TYO', 'HKG', 'IST', 'KUL', 'NYC', 'SFO', 'DBN'])


data = flight_data.flights_summary(iataCode_flights=flights)
print('Flight data summary: ' + str(data))

notification = NotificationManager(data)


