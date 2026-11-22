from movement import goto
from setups import *

def farm_sunflower(quota=200):
	while num_items(Items.Power) < quota:
		if num_items(Items.Carrot) < 1:
			print("Exhausted input!")
			return
		
		petals = set()
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				move(North)
				polyplant(Entities.Sunflower)
				petals.add(measure())
			move(East)
		
		while len(petals) > 0:
			most = max(petals)
			pluck(most)
			petals.remove(most)
