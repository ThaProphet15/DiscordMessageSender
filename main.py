import requests
import time

# Made by IntelScripter#8313
# Sends a message to a channel in a discord channel


payload = {
    'content': "messge here"
}

header = {
    'authorization': 'discord token'
}


r = requests.post("https://discord.com/api/v9/channels/CHANNELID/messages", data=payload, headers=header)
print("Sent")
