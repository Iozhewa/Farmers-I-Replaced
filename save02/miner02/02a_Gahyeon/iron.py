from movement import *
from setups import *

def iron():
	if get_ground_type() == Grounds.Iron:
		dig()

def farm_iron(fromTheTop=False, quota=50):
	change_hat(Hats.Bucket)
	if fromTheTop:
		clear()
	while num_items(Items.Iron) < quota:
		if num_items(Items.Coal) < 1:
			print("Exhausted input!")
			break
		goto()
		prospect = prospect_iron()
		while prospect != None:
			move(prospect)
			prospect = prospect_iron()
		if num_items(Items.Coal) >= 1:
			while get_ground_type() != Grounds.Iron:
				dig()
			while get_ground_type() == Grounds.Iron:
				dig()
