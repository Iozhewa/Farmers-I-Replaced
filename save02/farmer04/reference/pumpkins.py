def powerset_2(a, b):
	result = []
	for x in (a, b):
		for y in (a, b):
			spot = (x, y)
			result.append(spot)
	return result
corner_set = powerset_2(5, 11)  
# In expand IV, this was (2, 5)
# In expand  V, this was (3, 7)

def should_harvest(pos):
	p = can_harvest()
	q = get_entity_type() != Entities.Pumpkin
	r = pos in corner_set
	return p and (q or r)
	
def farm_pumpkin(quota=1000):
	change_hat(Hats.Gray_Hat)
	while num_items(Items.Pumpkin) < quota:
		for _ in range(get_world_size()):
			move(North)
			pos = (get_pos_x(), get_pos_y())
			if should_harvest(pos):
				harvest()
			if get_entity_type() == Grounds.Grassland:
				till()
			plant(Entities.Pumpkin)
			if num_items(Items.Water) > 0 and get_water() < 0.5:
				use_item(Items.Water)
		move(East)