def prepMaze(size=1):
	goto(size, size)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, size)

def projection(position, direction):
	x, y = position
	if direction == North:
		return (x, y + 1)
	elif direction == West:
		return (x - 1, y)
	elif direction == South:
		return (x, y - 1)
	else:  # Enumeration, has to be East
		return (x + 1, y)
def tryMaze(breakpoint=0):
	leftOptions = {North: West, West: South, South: East, East: North}
	positions = set()
	solved = False
	withPath = North
	limiter = 0
	while get_entity_type() == Entities.Hedge:
		if limiter > 4:
			quick_print("Retreading path..")
			tryMaze(breakpoint+1)  # Reset positions, reset 'POV'
		if breakpoint > 4:
			quick_print("Cannot solve maze!")
			while True:
				do_a_flip()
		positions.add(coord())
		quick_print(coord())
		if can_move(withPath):
			move(withPath)
		else:
			while not(can_move(withPath)):
				withPath = leftOptions[withPath]
			x, y = projection(coord(), withPath)
			if (x, y) in positions:
				withPath = leftOptions[withPath]
			limiter += 1
	harvest()

def stress(debug=False):
	if debug:
		tryMaze()
		return
	for i in range(1, 4):
		for j in range(1, 3):
			quick_print("Size:", i, "| Trial:", j)
			prepMaze(i)
			tryMaze()
			