#The below code simultes the famous paper,rock ,scissors game.
import random

data= ['rock','paper','scissors']

user = int(input('Enter 0 for rock, 1 for paper and 2 for scissors!\n'))

comp = random.randint(0,2)

if user <= 2: 
    if data[user] == 'scissors' and data[comp] == 'paper':
            print('You chose {} '.format(data[user]))
            print('The computer chose {} '.format(data[comp]))
            print('you win!')
            
    elif  data[comp]  == 'scissors' and data[user] == 'paper':
            print('You chose {} '.format(data[user]))
            print('The computer chose {} '.format(data[comp]))
            print('you lose!')
        
    elif data[user] == 'rock' and data[comp] == 'scissors':
            print('You chose {} '.format(data[user]))
            print('The computer chose {} '.format(data[comp]))
            print('you win!')
            
    elif  data[comp]  == 'rock' and data[user] == 'scissors':
            print('You chose {} '.format(data[user]))
            print('The computer chose {} '.format(data[comp]))
            print('you lose!')
        
    elif data[user] == 'paper' and data[comp] == 'rock':
            print('You chose {} '.format(data[user]))
            print('The computer chose {} '.format(data[comp]))
            print('you win!')
        
    elif  data[comp]  == 'paper' and data[user] == 'rock':
            print('You chose {} '.format(data[user]))
            print('The computer chose {} '.format(data[comp]))
            print('you lose!')
            
    else:
        print('You chose {} '.format(data[user]))
        print('The computer chose {} '.format(data[comp]))
        print('Issa Draw!')
    
else:
    print('Your selection is out of range, Try Again!')
