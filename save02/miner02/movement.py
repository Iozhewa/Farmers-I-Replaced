from setups import *


def goto(x=0, y=0):
	pos = (get_pos_x(), get_pos_y())
	if pos == (x, y):
		return
	if x < pos[0]:
		move(West)
	if pos[0] < x:
		move(East)
	if y < pos[1]:
		move(South)
	if pos[1] < y:
		move(North)
	goto(x, y)
	
def rotation():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			goto(x, y)
		move(North)