class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"The restaurant name is {self.restaurant_name}.")
		print(f"The restaurant cuisine type is {self.cuisine_type}")

	def open_restaurant(self):
		print(f"The restaurant is now openning")


class IceCreamStand(Restaurant):
	def __init__(self):
		self.flavors = ['milk','vanilla','chocolate']

	def describe_ice(self):
		#for i in self.flavors:
		f = ' '.join(self.flavors)
		print(f"We have the {f} icecream.")


icecream = IceCreamStand()
icecream.describe_ice()