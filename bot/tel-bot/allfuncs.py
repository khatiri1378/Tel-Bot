import os
import re
import requests
import time
from Varies import *

#reading Token
with open("../bot-token/token.txt", "r") as f:
    Token = f.readline()
    f.close()

#receive messages
def receive_message(self):

    textcolor = QColor(0, 255, 0)
    self.ReceiverDisplay.setTextColor(textcolor)
    while True:
        URL = 'https://api.telegram.org/bot'+Token+'/getupdates?offset=-1'
        req = requests.get(URL)
        #reading user id
        user_id = re.findall(r'{"id":(\w+),', req.text)
        if (user_id != []):
            User_id = user_id[0]

        else:
            self.ReceiverDisplay.append("error")
        #reading username
        user_name = re.findall(r'username":"(\w+)",', req.text)
        if (user_name != []):
            User_name = user_name[0]
        else:
            User_name = "Unknown"

        #reading users name
        name = re.findall(r'first_name":"(\w+)"',req.text)
        if (name != []):
            Name = name[0]
        else:
            Name = "Unknown"

        date = re.findall(r'},"date":(\w+),', req.text)


        text1 = re.findall(r',"text":"(\w)"}}]}', req.text)
        text2 = re.findall(r',"text":"(\w.+)"}}]}', req.text)
        text3 = text1 + text2
        if(text3 != []):
            Text = text3[0]
        else:
            Text = "*Error, can't Read Message...*"


        Final_Message = f"""

        New Message Received From User {User_id}
        Name : {Name}
        Username: @{User_name}
        Message :
        {Text}
        ------------------------------
        """
        self.ReceiverDisplay.append(Final_Message)
        break
