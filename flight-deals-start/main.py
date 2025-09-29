#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from dotenv import load_dotenv
import os
from data_manager import DataManager

load_dotenv()

sheety_data = DataManager(url=os.getenv("SH_URL"),auth=os.getenv("SH_AUTH"))

list = sheety_data.get_cities()

print(list)
