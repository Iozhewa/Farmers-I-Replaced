from movement import goto

def farm_sunflower(quota=800):
	change_hat(Hats.Traffic_Cone)
	while num_items(Items.Power) < quota:
		if num_items(Items.Carrot) < 1:
			print("Exhausted input!")
			return
		
		for _ in range(get_world_size()):
			move(North)
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			if num_items(Items.Water) > 0 and get_water() < 0.5:
				use_item(Items.Water)
		move(East)	