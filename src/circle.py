"""
Define a class structure for a Circle with static methods, class methods, 
instance methods, and properties via instance methods:
1. inherit from object,
2. include a base initializer that stores a radius and optional color,
3. method to validate a color is "red", "green", or "blue",
4. method for creating a circle from a radius,
5. method for creating a circle from a circumference, 
6. method for calculating a circumference from a radius, 
7. method to return circumference of the circle,
8. method to return area of the circle,
9. method to return the area of a circle that accepts a scaling factor of the radius.
10. implement the following Circle method:
def area_scale_dict(self):
   '''
   Return a dictionary of circle radiuses (mapped to area) of the Circle from 10% 
   of the radius up to 100% (the radius), incrementing by 5% with each step.
   '''
"""
import pdb
from math import pi
import matplotlib.pyplot as plt

class Circle(object):

	def __init__(self, r, c=None):
		if c is None:
			self.radius = r
		else:
			self.radius = r
			self.color = c.lower()

	def is_primary_color(self):
		if (self.color == "red") or \
		(self.color == "green") or \
		(self.color == "blue"):
			return True
		else:
			return False

	def draw(self):
		circle1 = plt.Circle( (0.5,0.5), self.radius, color="blue", fill=False)
		fig, ax = plt.subplots()
		ax.add_artist(circle1)
		fig.savefig('plotcircles.png')

	def circumference(self):
		return 2 * pi * self.radius

	def area(self):
		return pi * self.radius**2

	def scaling_factor_area(self, factor):
		return pi * (self.radius * factor)**2

	def area_scale_dict(self):
		'''
	   	Return a dictionary of circle radiuses (mapped to area) of the Circle from 10% 
	   	of the radius up to 100% (the radius), incrementing by 5% with each step.
	   	'''
		dictionary = {}
		percentage = 0.10

		while (percentage <= 1.00):
	   		rad = self.radius * percentage
	   		dictionary[rad] = pi * rad**2
	   		percentage += 0.05

		return dictionary



	def set_radius(self, r):
		self.radius = r

	def set_color(self, c):
		self.color = c


# pdb.set_trace()
# exec(open("./src/circle.py").read())

