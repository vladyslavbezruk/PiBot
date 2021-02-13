import requests

API_link = "https://api.telegram.org/bot1587405934:AAEAKvidxADTdlu_Pr0w8TQHpO-QV7T4uEM"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]
test = message["text"]

sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Hello world")

