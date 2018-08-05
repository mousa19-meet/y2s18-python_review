# Write your solutions for 1.5 here!

class Superhero:
	def __init__(self,name,strength,superpower):
		self.superpower = superpower
		self.name = name 
		self.strength = strength

	def print2(self):
		print(self.name + " " +str(self.strength))

	def save(self,work):
		if work <= self.strength:
			self.strength -= work 
			print("strength is now " + str(self.strength))
		else:
			print("not strong enough :(")


super1 = Superhero("mousa" , 10 , "flying")

super1.save(20)
