from processor import process

def goto(x, y):
	if x < get_pos_x():
		move(West)
	elif x > get_pos_x():
		move(East)
	elif y < get_pos_y():
		move(South)
	elif y > get_pos_y():
		move(North)
	else:
		return
	goto(x, y)
	
def snake_run(request="simple"):
	lane = get_world_size()-1
	upDown = {North: South, South: North}
	direction = North
	for _ in range(lane+1):
		for _ in range(lane):
			move(direction)
			process(request)
		move(East)
		process(request)
		direction = upDown[direction]

def poly_shift(cropsLeft=get_world_size()**2):
	if cropsLeft == 0:
		return
	else:
		ox, oy = (get_pos_x(), get_pos_y())
		companion, (x, y) = get_companion()
		goto(x,y)
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Soil:
			till()
		elif companion == Entities.Carrot and get_ground_type() == Grounds.Grassland:
			till()
		plant(companion)
		goto(ox, oy)
		harvest()
		poly_shift(cropsLeft-1)

def work_shift(request="simple", squareOf=2):
	if request in {"pumpkin", "pumpkin_charge"}:
		snail_run(request, 3)
	else:
		snake_run(request)
	if request not in {"simple", "collect", "plow"}:
		snake_run("collect")

curl = {East: North, North: West, West: South, South: East}
def snail_stroll(request, side, direction=East):
	for _ in range(4):
		for _ in range(side):
			process(request)
			move(direction)
		direction = curl[direction]
	move(East)
	move(North)

toMake = {2: (6, 2, 1), 3: (4, 3, 2)} 
#  Experimental: (3, 4, 3), (2, 6, 4), (1, 12, 5)
def snail_run(request="simple", squareOf=2):
	strolls, step, side = toMake[squareOf]
	for x in range(strolls):
		goto(step*x,0)
		for y in range(strolls):
			goto(step*x, step*y)
			snail_stroll(request, side)

def mole_run(request="coal"):
	while get_ground_type() != Grounds.Clay:
		for x in range(0, 12):
			if x % 2 == 0:
				y = 5
			else:
				y = 6
			goto(x, y)
			dig()
			dig()  # 1 dig is lossless, 2 digs potentially lossy
		snake_run(request)
		if request == "iron":
			break

def carabao_run(request="rice"):
	while get_ground_type() != Grounds.Clay:
		mole_run()
	while get_ground_type() != Grounds.Rock:
		snake_run(request)
	snake_run("collect")

def golem_run(request="iron", quota=15):
	while get_ground_type() != Grounds.Rock:
		mole_run("iron")
	if get_ground_type() == Grounds.Loam:
		print("Halting!")
		return
	while num_items(Items.Coal) > 0 and num_items(Items.Iron) < quota:
		while get_ground_type() != Grounds.Iron:
			prospect = prospect_iron()
			if prospect != None:
				move(prospect)
			else:
				dig()
		dig()
		for _ in range(2):
			mole_run("iron")
