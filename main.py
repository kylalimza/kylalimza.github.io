  
import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Update has been made to the kylalimza.github.io repository! Check it out!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+os.environ['to_whatsapp_no']
                          )

print("Message ID:",message.sid)
