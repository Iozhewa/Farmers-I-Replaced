from movement import goto

def myMax(a, b):
	if a >= b:
		return a
	return b

def maxP(petals):  # Works for non-empty lists
	rest = petals
	rest.pop(0)
	if len(petals) == 1:
		return petals[0]
	else:
		return myMax(petals[0], maxP(rest))

def farm_sunflower(quota=800):
	while num_items(Items.Power) < 200:
		if num_items(Items.Carrot) < 1:
			print("Exhausted input!")
			break
		
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
			
		petals = []  # List of [x, y, petal]
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				move(North)
				metric = (x, y, measure())
				petals.append(metric)
				quick_print(petals)
			move(East)
		quick_print(".")
		
		while len(petals) > 0:
			if (num_items(Items.Power)) < quota:
				break
			x, y, metric = maxP(petals)
			quick_print(petals)
			goto(x, y)
			harvest()
			petals.remove(maxP(petals))