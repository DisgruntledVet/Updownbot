import requests, webbrowser
import json

#created by the disgruntledVet

#follow incoming webhook instructions to recieve url @here https://api.slack.com/incoming-webhooks
def send_email():
    web_hook_url = 'insert incoming webhook url'

    slack_msg = {'text': 'The content has been removed' + page.url}

    requests.post(web_hook_url,data=json.dumps(slack_msg))

#the same webhook url for send_email is used @here as well
def send_email2():
    web_hook_url = 'insert incoming webhook url'

    slack_msg = {'text': 'The content is still up' + page.url}

    requests.post(web_hook_url,data=json.dumps(slack_msg))

# calls the csv for urls
f = open("tester2.csv", "r")
for url in f:
  page = requests.get(url)

   
   # checks if pages/content are down or up.
  if  page.status_code == 404 or page.url == 'https://twitter.com/account/suspended%0A':
   	   print('gotem', page.url)
   	   send_email()
   	  


  else:
   		print ('still up', page.url)
   		send_email2()
