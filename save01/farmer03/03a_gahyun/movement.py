from manual import process

def goto(x=0, y=0):
	px, py = (get_pos_x(), get_pos_y())
	if x < px:
		move(West)
	elif x > px:
		move(East)
	elif y < py:
		move(South)
	elif y > py:
		move(North)
	else:
		return
	goto(x, y)

def diagonal(x0=0, request="simple"):
	lane = get_world_size()-1
	goto(x0, 0)
	process(request)
	while get_pos_x() > 0:
		move(North)
		move(West)
		process(request)
	goto(x0, lane)
	process(request)
	while get_pos_x() < lane:
		move(South)
		move(East)
		process(request)

def l_shape(n=0, request="simple"):
	lane = get_world_size()-n
	goto(n, n)
	process(request)
	for y in range(lane+n):
		goto(n, y)
		process(request)
	for x in range(lane+n):
		goto(x, n)
		process(request)

def zig(request="simple"):
	lane = get_world_size()
	for x in range(lane):
		for y in range(lane):
			if x % 2 == 0:
				goto(x, y)
			else:
				goto(x, lane-1-y)
			process(request)
		process(request)
	move(East)

def run(request="simple", func=zig):
	if func == zig:
		func(request)
		return
	for i in range(get_world_size()):
		func(i, request)
