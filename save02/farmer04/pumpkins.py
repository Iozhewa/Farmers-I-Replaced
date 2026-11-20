from setups import *

def powerset_2(a, b):
	result = []
	for x in (a, b):
		for y in (a, b):
			spot = (x, y)
			result.append(spot)
	return result
corner_set = powerset_2(7, 15)  
# In expand IV, this was (2, 5)
# In expand  V, this was (3, 7)
# In expand VI, this was (5, 11)

def should_harvest(pos):
	p = can_harvest()
	q = get_entity_type() != Entities.Pumpkin
	r = pos in corner_set
	return p and (q or r)
	
def farm_pumpkin(quota=1000):
	while num_items(Items.Pumpkin) < quota:
		for _ in range(get_world_size()):
			move(North)
			pos = (get_pos_x(), get_pos_y())
			if should_harvest(pos):
				harvest()
			polyplant(Entities.Pumpkin)
		move(East)