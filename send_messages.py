# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACf4c2a663f57bc6dd5e1565afb3e46ec2"
auth_token = "e381cc4902fe3f661ab7769a34aef666"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+918947897494",
                                             from_="+12565675123",
                                             body="Hi, Sleep soon. Love, Sonal")
