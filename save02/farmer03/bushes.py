def farm_bush(quota=100):
	change_hat(Hats.Purple_Hat)
	while num_items(Items.Wood) < quota:
		for _ in range(get_world_size()):
			move(North)
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Grassland:
				till()
			plant(Entities.Bush)
		move(East)