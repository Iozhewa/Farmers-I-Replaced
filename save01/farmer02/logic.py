def collect():
	if can_harvest():
		harvest()

def plow():
	collect()
	if get_ground_type() == Grounds.Grassland:
		till()

def water(expected=0.1, fully=False):
	if get_water() < expected:
		use_item(Items.Water)
	while get_water() < expected:
		use_item(Items.Water)

def reserved(n=0):
	x, y = (get_pos_x(), get_pos_y())
	return (x + y) % n == 0

def carrot(withCharge=False):
	plow()
	water()
	if withCharge and reserved(3):
		plant(Entities.Sunflower)
	elif not(reserved(3)):
		plant(Entities.Carrot)
	else:
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Bush)

def tree(withCharge=False):
	collect()
	if get_ground_type() == Grounds.Soil:
		till()
		
	if withCharge and not(reserved(2)):
		till()
		plant(Entities.Sunflower)
	elif reserved(2):
		plant(Entities.Tree)
		water(0.25, True)
	else:
		plant(Entities.Bush)


counter = 0
squareToggle = False
def pumpkinSquare():
	if counter % 9 == 0:
		global squareToggle
		squareToggle = not(squareToggle)
	return squareToggle

def pumpkin(withCharge=False):
	plow()
	water()
	if pumpkinSquare():
		plant(Entities.Pumpkin)
	elif withCharge:
		plant(Entities.Sunflower)
	else:
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Bush)
	global counter
	counter += 1

def coal():
	if get_ground_type() == Grounds.Coal:
		dig()

def rice():
	ground = get_ground_type()
	if ground == Grounds.Rock:
		return
	elif ground == Grounds.Clay:
		plant(Entities.Rice)
	elif can_harvest():
		harvest()
	else:
		dig()

def iron():
	if get_ground_type() == Grounds.Iron:
		dig()