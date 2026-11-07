from processor import *

def goto(x, y):
	while get_pos_x() != x:
		move(West)
	while get_pos_y() != y:
		move(South)
def coord():
	return (get_pos_x(), get_pos_y())

def run(request, spec=6):
	lane = get_world_size()-1
	process(request, spec)
	for _ in range(lane):
		move(North)
		process(request, spec)
	move(East)
	process(request, spec)
	for _ in range(lane):
		move(South)
		process(request, spec)
	move(East)
	