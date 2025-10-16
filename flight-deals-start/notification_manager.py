from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,cheap_flights_lst:list):
        self.cheap_flights_lst = cheap_flights_lst
        self.send_notifications()

    def send_notifications(self): # 
        '''cheap_flights_lst is of the form [{source:___,
        destination:___,
        departure_time:___,
        arrival_time:___,
        price:___
        }
        ] '''
        for flight in self.cheap_flights_lst:

            message_body = f"Low price alert! Only £{flight.get('price')} to fly from\
                  {flight.get('source')} to {flight.get('destination')}\
                    , on {flight.get('departure_time')} until {flight.get('arrival_time')}" #make the message for each flight
            
            api_key_sid = os.environ["TWILIO_KEY_SID"]
            api_key_secret = os.environ['TWILIO_KEY_SECRET']
            account_sid = os.environ['TWILIO_ACC_SID']   # Your Twilio account SID
            client = Client(api_key_sid, api_key_secret, account_sid)

            message = client.messages.create(
            from_= f'whatsapp:{os.environ["WHATS_APP_FROM_NUM"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["WHATS_APP_TO_NUM"]}'
            )
            print(message.status)



