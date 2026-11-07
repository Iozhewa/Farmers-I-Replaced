def collect():
	if can_harvest():
		harvest()
		
def raze():
	if can_harvest():
		harvest()
	till()

def rice():
	if can_harvest():
		harvest()
	elif get_ground_type() == Grounds.Clay:
		plant(Entities.Rice)  # Note terraces dry out
	else:
		if get_ground_type() == Grounds.Rock:
			return
		dig()
		
def coal():
	if get_ground_type() == Grounds.Coal:
		dig()

def goto(x, y):
	#  goto in movement reverses directions, this version delivers faster code with og dirs
	while x != get_pos_x():
		move(East)
	while y != get_pos_y():
		move(North)

def poly():
	if can_harvest():
		harvest()
	if get_ground_type() == Grounds.Soil:
		quick_print("Carrot defaulted!")
		plant(Entities.Carrot)
		return
	if get_water() < 0.25:
		quick_print("Watered!")
		use_item(Items.Water)

	ox, oy = (get_pos_x(), get_pos_y())
	quick_print("Working on: (", ox, ",", oy, ")")
	companion, (x, y) = get_companion()
	if companion == None:
		if num_items(Items.Carrot) > 1000:
			quick_print("Sunflower defaulted!")
			plant(Entities.Sunflower)
		else:
			goto(ox, oy)
			return
	goto(x, y)
	if companion == Entities.Carrot:
		till()
		if get_ground_type() == Grounds.Soil:
			plant(companion)
	else:
		plant(companion)
	goto(ox, oy)

#  needs improvement
grid = {2: {1, 3, 5, 7, 11}, 3: {2, 5, 8, 11}, 4: {3, 7, 11}, 6: {5, 11}}

def gridline(mode=6):
	x, y = (get_pos_x(), get_pos_y())
	xPredicate = x != 0 and x % mode == 0
	yPredicate = y != 0 and y % mode == 0
	return xPredicate or yPredicate

def cropCorner(mode=6):
	x, y = (get_pos_x(), get_pos_y())
	cornerSet = grid[mode]
	return x in cornerSet and y in cornerSet

def charged(mode=6):
	if num_items(Items.Carrot) < 1000:
		print("Load carrots!")
		return
	if get_entity_type() in {Entities.Grass, Entities.Sunflower} or cropCorner(mode):
		harvest()
		till()
		if get_ground_type() == Grounds.Grassland:
			harvest()
			till()
	if get_water() < 0.10:
		use_item(Items.Water)
	
	if gridline(mode):
		plant(Entities.Sunflower)
	else:
		plant(Entities.Pumpkin)

def bushed(mode=6):
	if can_harvest():
		harvest()
	
	if gridline(mode):
		plant(Entities.Bush)
	else:
		till()
		if get_ground_type() == Grounds.Soil:
			use_item(Items.Water)
			plant(Entities.Carrot)
	if get_water() < 0.10:
		use_item(Items.Water)