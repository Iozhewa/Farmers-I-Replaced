def farm_carrot(quota=80):
	change_hat(Hats.Green_Hat)
	while num_items(Items.Carrot) < quota:
		if num_items(Items.Hay) < 1 or num_items(Items.Wood) < 1:
			print("Exhausted input!")
			break
		
		for _ in range(get_world_size()):
			move(North)
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrot)
			if num_items(Items.Water) > 0 and get_water() < 0.5:
				use_item(Items.Water)
		move(East)