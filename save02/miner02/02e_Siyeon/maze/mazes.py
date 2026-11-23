from setups import *
from movement import *
from solutions import *

mid = get_world_size()/2
def setup(size=1):
	if num_drones() == 1:
		goto(mid, mid)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, size)

def farm_treasure(quota=5000, limit=get_world_size()-1):
	change_hat(Hats.Gold_Hat)
	counter = 1
	spot = (get_pos_x(), get_pos_y())
	while num_items(Items.Gold) < quota:
		collect()
		goto(spot[0], spot[1])
		setup(counter)
		if counter == 1:
			trivial_solution()
		else:
			left_hand_rule()
		if counter == limit:
			counter = 1
		else:
			counter += 1
		
if __name__ == "__main__":
	collect()
	setup(9)
	left_hand_rule()