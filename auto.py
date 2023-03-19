import os
import re
import requests
import time

File = open('token.txt', 'r')
for token in File :
    time.sleep(0.1)

Token = token.strip('\n')
t = ''

# answers:

hi = ['hello', 'hi', 'salam', 'hey']
bye = ['bye', 'tata', 'goodbye', 'khodafez']


while True:

    URL = 'https://api.telegram.org/bot'+Token+'/getupdates?offset=-1'
    req = requests.get(URL)
    user_id = re.findall(r'{"id":(\w+),', req.text)
    if (user_id != []):
        User_id = user_id[0]

        text1 = re.findall(r',"text":"(\w)"}}]}', req.text)
        text2 = re.findall(r',"text":"(\w.+)"}}]}', req.text)
        text3 = text1 + text2
        

        
        def answer(ans):
            req = requests.get('https://api.telegram.org/bot'+ Token +'/sendMessage?chat_id='+ User_id +'&text='+ ans)
            if (req.status_code == 200):
                print ('message send to '+User_id+' Sucessfully')
        c = 0
        for i in text3:
            c = c + 1
        if (c != 0):
            Text = text3[0]
            if (Text != t):
                
                if (Text in hi):
                    answer('hello')

                if ('notepad' in Text):
                    os.system('Notepad')

                if ('firefox' in Text):
                    os.system('start firefox')

                if (Text in bye):
                    answer('bye')

                if (Text == 'average'):
                    answer('Send Numbers:')
                    time.sleep(5)
                    su = 0
                    counter = 0
                    Num = 0
                    while True:
                        
                        req = requests.get(URL)
                        text1 = re.findall(r',"text":"(\w)"}}]}', req.text)
                        text2 = re.findall(r',"text":"(\w.+)"}}]}', req.text)
                        text3 = text1 + text2
                        num = text3[0]
                        if (num == 'end' or num == 'average'):
                            break
                        
                        num = int(num)
                        if (num != Num):
                            answer('Number Received!')
                            su = num + su
                            counter = counter + 1
                            Num = num
                    if (counter != 0):
                        avr = float(su / counter)
                        avr = str(avr)
                         
                        answer('Average: '+ avr)
                    else:
                        answer('No Number Received! \nAverage: 0.00')


                
                
        else:
            Text = ''







    

            



        t = Text

    else:
        print ('No Message...')
        time.sleep(5)
