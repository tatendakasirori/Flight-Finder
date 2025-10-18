#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from dotenv import load_dotenv
import os
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

load_dotenv()
#FlightSearch object for talking to the flight search api
flights_search = FlightSearch(amad_api=os.getenv("AMAD_API"), amad_api_secret=os.getenv("AMAD_API_SECRET"))

#Check if google sheet's iataCodes column needs updating
sheety_data = DataManager(url=os.getenv("SH_URL"),auth=os.getenv("SH_AUTH"))
if sheety_data.needs_iatacodes():
    #get the list of cities in the google sheet
    list = sheety_data.get_cities()

    #get iatacodes for the cities in list using the FlightSearch object
    iatacodes = flights_search.get_iatas(list)

    #enter the iatacodes into the google sheets
    sheety_data.write_iata(iatacodes)

###########ALGORITHM##########
''' Flight_search.get_flights(list of iatacodes) -> FlightData.filter_by_price(flights from Flight_search)'''

#make citydata_dict used in getting flights
citydata_dict = sheety_data.make_citydata_dict()

#search for flights with given parameters
flights = flights_search.get_flights(iata_codes=sheety_data.get_iatacodes())

#filter by price and summariz flight data using FlightData object
flight_data = FlightData(citydata_dict=citydata_dict)


data = flight_data.flights_summary(iataCode_flights=flights)
print('Flight data summary: ' + str(data))

#Send notifications of found flights
notification = NotificationManager(data)


