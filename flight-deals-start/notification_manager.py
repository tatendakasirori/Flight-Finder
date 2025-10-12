from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    message_body = f"{STOCK}: {stock_change.percentage_change}\nHeadline: {article['title']}\nBrief: {article['description']}"
    account_sid = os.environ["TWILIO_ACC_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_= os.environ["WHATS_APP_FROM_NUM"],
    body=message_body,
    to=os.environ["WHATS_APP_TO_NUM"]
    )
    print(message.status)