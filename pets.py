def describe_pet(pet_name,animal_type='dog'):
	"""describe infomation of pet"""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s is {pet_name.title()}。\n")

describe_pet(pet_name='harry')
describe_pet(animal_type='dog',pet_name='willie')

