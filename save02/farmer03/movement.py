def goto(x=0, y=0):
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