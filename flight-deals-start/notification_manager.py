from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_notifications(cheap_flights_lst:list): # 
        '''cheap_flights_lst is of the form [{soure:__,
        destination:___,
        departure:___,
        arrival:___
        }
        ]'''
        for flight in cheap_flights_lst:
            message_body = f"Low price alert! Only {flight.get('price')} to fly from\
                  {flight.get('source')} to {flight.get('destination')}\
                    , on {flight.get('departure')} until {flight.get('arrival')}"
            account_sid = os.environ["TWILIO_ACC_SID"]
            auth_token = os.environ["TWILIO_AUTH_TOKEN"]
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_= os.environ["WHATS_APP_FROM_NUM"],
            body=message_body,
            to=os.environ["WHATS_APP_TO_NUM"]
            )
            print(message.status)