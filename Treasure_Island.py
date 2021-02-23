#Fun code for treasure hunt

print('Welcome to Treasure Island.May the odds be in your favour!')
print("Your mission is to find the treasure.") 
print()
print('You are at a crossroad')

direction = input('Which direction do you want to go? L or R: ').upper()

#logic for the game
if direction == 'L':
    print('You get to a river, what do you do? ')
    action = input('Do you want to swim or wait? S or W: ').upper()
    
    if action == 'W':
        print('Infront of you, you see 3 doors, which one do you enter?')
        door = input('Blue, yellow or red? ').lower()
        
        if door == 'yellow':
            print('Congratulations! You found the Treasure.')
        else:
            print('Deadly snakes, Game Over!')
    else:
        print('The river is full of crocodiles.Game over!')
        

else:
    print('Ooops! Dead end. Game over')

#can make the game as complex as possible
