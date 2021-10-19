import os
import requests
from termcolor import colored
import time

os.system('cls')
os.system('clear')

# reading token :

print (colored('Reading Your Bots Token From ', 'green')+colored('token.txt', 'yellow'))
File = open('token.txt', 'r')

for token in File :
    print (colored('Please wait...', 'white'))
Token = token.strip('\n')
time.sleep(1)
print (colored('\nYour Token Is : ', 'yellow')+Token)
print (colored('\nnote : ', 'red')+colored('if its not your token check the token.txt file', 'yellow'))
for i in range(0,5):
    print ('.')
    time.sleep(1)
os.system('clear')
os.system('cls')
    
print (colored('''Welcome\n
How Can I Help You?
''', 'green'))

print (colored('''1.Send Message To One User

2.Send Message To All Users
''', 'yellow'))
ch = input (colored('# ', 'red'))
ch = str(ch)

# wrong inputs :

while (ch != '1' and ch != '2'):
    print (colored('Incorrect', 'red'))
    time.sleep(1)
    os.system('cls')
    os.system('clear')
    
    print (colored('''Welcome\n
How Can I Help You?
''', 'green'))

    print (colored('''1.Send Message To One User

2.Send Message To All Users
''', 'yellow'))
    ch = input (colored('# ', 'red'))
    ch = str(ch)

# sending message to one user :

if (ch == '1'):
    User_id = input (colored('\nEnter User id :\n', 'green')+colored('\n# ', 'red'))
    print (colored('\nUser Set : ', 'yellow')+User_id)
    print (colored('\nWrite Your Message Here :\n', 'green'))
    while True :
        Text = input (colored('# ', 'red'))
        req = requests.get('https://api.telegram.org/bot'+ Token +'/sendMessage?chat_id='+ User_id +'&text='+ Text)
        if (req.status_code == 200):
            print (colored('\nYour Message Sent Sucessfully\n', 'red', 'on_green'))
        else :
            print (colored('Sorry, We cant Send Your Message Now...\n', 'white', 'on_red')+colored('Please Try Again Later ):', 'red'))


#sending message to all users :

if (ch == '2'):
    file = open('userids.txt', 'r')
    print (colored('This Is The List Of Your Users :\n', 'yellow'))
    for users in file:
        print (colored(users, 'green'))
        time.sleep(0.5)
    while True :
        print (colored('\nWrite Your Message Here :\n', 'green'))
        Text = input (colored('# ', 'red'))
        print (colored('\nStart Sending Your Message\nPlease Wait...', 'green'))
        time.sleep(2)
        File = open('userids.txt', 'r')
        for User_id in File:
            req = requests.get('https://api.telegram.org/bot'+ Token +'/sendMessage?chat_id='+ User_id +'&text='+ Text)
            if (req.status_code == 200):
                print (colored('Message Sent To User :', 'red', 'on_green')+' '+User_id)
            else :
                print (colored('Faild To Send Message :', 'white', 'on_red')+' '+User_id)
        print (colored('Finished.', 'green'))    
        
