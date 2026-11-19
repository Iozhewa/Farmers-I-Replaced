def farm_hay(quota = 100):
	change_hat(Hats.Brown_Hat)
	while num_items(Items.Hay) < quota:
		for _ in range(get_world_size()):
			move(North)
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Grassland:
				till()
		move(East)