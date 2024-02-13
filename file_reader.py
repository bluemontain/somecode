filename = 'pi_miline.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	#for line in file_object:
	#	print(line.rstrip())
	#contents = file_object.read()
pi_string = ''
for line in lines:
	pi_string += line.strip()


birthday = input("Enter your birthday：")

if birthday in pi_string:
	print("Your birthday in the first 200miline pi")
else:
	print("Your birthday not in the first 200miline pi")
#print(f"{pi_string[:100]}...")
#print(len(pi_string))
	


