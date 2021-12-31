print('Give me two numbers, and I\'will divide them')
print('Enter \'q\' to quit')
while True:
	first_number=input('\nfirst_number:')
	if first_number=='q':
		break
	second_number=input('second_number:')
	if second_number=='q':
	    break
	try:
	    answer=int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("you can't division by zero")
	else:
	    print(answer)    	
