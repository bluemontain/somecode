from random import randint

class Die:
	def __init__(self,sides):
		self.sides = sides

	def roll_die(self):
		

	    roll_out = randint(1,self.sides)
	    print(roll_out)


d = Die(20)
d.roll_die()