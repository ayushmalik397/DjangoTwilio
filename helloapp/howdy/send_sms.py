from twilio.rest import Client

def send(number, name):
    text_to_send = "Hello! Mr./Mrs. "+name+" is coming to your appartment"
    account_sid = 'ACdaa6bc9c6e6a6ae060e3b8df52aa4eff'
    auth_token = '6295cc3f4f569d4e80a826dc01b627d0'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=text_to_send,
                         from_='+17755574512',
                         to=number
                     )
