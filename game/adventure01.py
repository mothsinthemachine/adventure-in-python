# main.py -- The main Python program that runs the game

# Display title screen
print('''\n
---------------------------------
          It's time for
       A D V E N T U R E !
---------------------------------\n\n''')

# Display the title menu
print('----------Title Menu----------')
print('1. Start a new adventure')
print('2. Resume a previous adventure')
print('0. Quit')
choice = input('Enter a number for the choice: ')
#print(choice)
#datatype = str(type(choice))
#print(choice + ' is data type of ' + datatype)

if choice == '1':
	print('Starting a new adventure...')
elif choice == '2':
	print('Resuming a previous adventure...')
elif choice == '0':
	print('Quitting... The game will now exit. Have nice day!\n\n')
else:
	print('Incorrect choice. Please chose a number from the menu.')