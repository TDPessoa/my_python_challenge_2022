"""
Function for checking if a str contains a selected group of characters.

@TDPessoa
"""


def name_check():
	username = str(input('Enter your username:'))
	rec = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '!', '@', '#', '$', '%', '&', '*', '(', ')', '_',
			'+', '/', '?']

	for c in range(len(username)):
		if (username[c] in rec):
			print('Username is not allowed.')
			return False

		else:
			print('Username is allowed')
			return True

while True:
	if (name_check() == True):
		confirm = str(input('Confirm? Y - Yes | else - No'))

		if confirm == "Y":
			break

		else:
			pass