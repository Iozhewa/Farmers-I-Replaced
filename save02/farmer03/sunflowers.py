from movement import goto

def myMax(a, b):
	if a[2] >= b[2]:
		return a
	return b

def maxP(petals):  # Works for non-empty lists
	if len(petals) == 0:
		return
	elif len(petals) == 1:
		return petals[0]
	else:
		rest = petals
		rest.pop(0)
		return myMax(petals[0], maxP(rest))

def farm_sunflower(quota=800):
	change_hat(Hats.Traffic_Cone)
	while num_items(Items.Power) < quota:
		if num_items(Items.Carrot) < 1:
			print("Exhausted input!")
			return
		
		for _ in range(get_world_size()):
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
			
		if (num_items(Items.Power)) >= quota:
			return
		petals = []  # List of [x, y, petal]
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				move(North)
				metric = (x, y, measure())
				petals.append(metric)
				quick_print(petals)
			move(East)
		quick_print(".")
		
		for _ in petals:
			x, y, metric = maxP(petals)
			quick_print(petals)
			goto(x, y)
			harvest()
			petals.remove(maxP(petals))