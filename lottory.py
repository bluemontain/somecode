from random import choice,sample




list_number = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e']

result = sample(list_number,4)

ticket_number = "".join(result)

#print(f"the number is {ticket_number}")

for i in range(40000):
	rand_number = "".join(sample(list_number,4))
	if ticket_number == rand_number:
		print(f"You got lottry by {i} choice.")


