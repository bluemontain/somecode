from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
	first = input("\nPleast give a first name.")
	if first == 'q':
		break
	last = input("\nPleast give a last name.")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first,last)
	print({formatted_name})