driving = input('Have you ever driven a car? (Y/N) ')
if driving != 'Y' and driving != 'N':
	print('You can only enter Y or N !!! ')
	raise SystemExit
age = int(input('How old are you? '))
if driving == 'Y':
	if age >= 18:
		print('You pass the test! ')
	else:
		print('It\'s weired. Why have you ever driven a car?')
elif driving == 'N':
	if age >= 18:
		print('You can go to the driver\'s license test.')
	else:
		print('That\'s alright. you can take the driver\'s license test few years later.')