def goto(x, y):
	pos = (get_pos_x(), get_pos_y())
	if (pos == (x, y)):
		return
	if pos[0] < x:
		move(East)
	if pos[0] > x:
		move(West)
	if pos[1] < y:
		move(North)
	if pos[1] > y:
		move(South)
	goto(x, y)