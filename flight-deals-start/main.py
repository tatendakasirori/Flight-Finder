#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from dotenv import load_dotenv
import os
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()

sheety_data = DataManager(url=os.getenv("SH_URL"),auth=os.getenv("SH_AUTH"))

list = sheety_data.get_cities()

flights = FlightSearch(amad_api=os.getenv("AMAD_API"), amad_api_secret=os.getenv("AMAD_API_SECRET"))
response = flights.get_iatas(list)
print(response)
