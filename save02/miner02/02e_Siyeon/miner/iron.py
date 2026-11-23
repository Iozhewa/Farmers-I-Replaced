from movement import *
from setups import *

def iron():
	if get_ground_type() == Grounds.Iron:
		dig()

def farm_iron(quota=50):
	change_hat(Hats.Bucket)
	goto()
	while num_items(Items.Iron) < quota:
		if num_items(Items.Coal) < 1:
			print("Exhausted input!")
			return
		prospect = prospect_iron()
		while prospect != None:
			move(prospect)
			prospect = prospect_iron()
		counter = 0
		while get_ground_type() == Grounds.Iron or counter < 5:
			dig()
			counter += 1
