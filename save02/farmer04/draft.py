from movement import goto
from setups import *

def plow(preferred=Grounds.Soil, strict=False):  # For illustrative purposes, from setups
	if not(strict):
		collect()
	if get_ground_type() != preferred:
		till()

def water(preferred=0.5):  # For illustrative purposes, from setups
	if get_water() < preferred:
		use_item(Items.Water)

def pluck(petals=11):  # For illustrative purposes, from movement
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			move(East)
			if measure() == petals:
				harvest()
		move(North)

def farm_sunflower(quota=200):
	while num_items(Items.Power) < quota:
		if num_items(Items.Carrot) < 1:
			print("Exhausted input!")
			return
		
		petals = set()
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				move(North)
				plow(Grounds.Soil)
				plant(Entities.Sunflower)
				water()
				petals.add(measure())
			move(East)
		
		while len(petals) > 0:
			most = max(petals)
			pluck(most)
			petals.remove(most)
