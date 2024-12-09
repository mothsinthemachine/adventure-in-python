# main.py -- The main Python program that runs the game

# Wrap main code in a main() function
def main():
	# Display title screen
	print('''\n
	---------------------------------
			It's time for
		A D V E N T U R E !
	---------------------------------\n\n''')

	choice = '' # Prime choice with an empty string
	while not choice == '0':
		# Display the title menu
		print() # Prints an empty line
		print('----------Title Menu----------')
		print('1. Start a new adventure')
		print('2. Resume a previous adventure')
		print('0. Quit')
		choice = input('Enter a number for the choice: ')

		if choice == '1':
			print('Starting a new adventure...')
			start_game()
		elif choice == '2':
			print('Resuming a previous adventure...')
		elif choice == '0':
			print('Quitting... The game will now exit. Have nice day!\n\n')
		else:
			print('Incorrect choice. Please chose a number from the menu.')


# Starting a new adventure
def start_game():
	print('''\n
You find yourself in a dark room, dimly lit by sunlight that
trickles in around the cracks and crevices between old wood
planks and dusty window curtains.

In such an place, there is one question on your mind.\n\n''')
	while True:
		try:
			raw_input = input('What is your name?: ')
			player_name = raw_input.capitalize()
			print('Your name is ' + player_name + '.')
			confirm = input('Is this correct? (y/n): ')
			if confirm.lower() == 'y':
				print('You are now known as ' + player_name + '.')
				return # return will break from the loop
			else:
				print('Let us try again.\n')
		except:
			print('\n(!) An error occurred while creating a player name.')
			print('Returning you to the title menu.')
			return


# Invoke main()
main()