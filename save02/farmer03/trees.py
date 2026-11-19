def farm_tree(quota=200):
	change_hat(Hats.Straw_Hat)
	while num_items(Items.Wood) < quota:
		for _ in range(get_world_size()):
			sum = get_pos_x() + get_pos_y()
			move(North)
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Grassland:
				till()
			if sum % 2 == 0:
				plant(Entities.Bush)
			else:
				plant(Entities.Tree)
		move(East)