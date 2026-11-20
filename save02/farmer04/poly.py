from movement import *
from setups import *

half_length = get_world_size() / 2
def visit(x=0, y=0):
	pos = (get_pos_x(), get_pos_y())
	directions = [North, East]
	if pos == (x, y):
		return
	delta_x = abs(pos[0] - half_length)
	delta_y = abs(pos[1] - half_length)
	if max(pos[0], delta_x) == delta_x:
		directions[1] = West
	if max(pos[1], delta_y) == delta_y:
		directions[0] = South
	while get_pos_x() != x:
		move(directions[1])
	while get_pos_y() != y:
		move(directions[0])

def poly_farm(plant=Entities.Grass, quota=5.4*10**4):
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			visit(x, y)
			if num_items(Entities.Grass) >= quota:
				return
			polyplant(plant)
			companion, spot = get_companion()
			if companion != None:
				visit(spot[0], spot[1])
				polyplant(companion)
				visit(x, y)
		move(North)