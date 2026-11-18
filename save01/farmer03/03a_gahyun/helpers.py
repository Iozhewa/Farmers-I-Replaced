def water(expected=0.25):
	if get_water() < expected:
		use_item(Items.Water)

def reserved(spot=2, align="_"):
	x, y = (get_pos_x(), get_pos_y())
	if align == "x":
		x = 0
	if align == "y":
		y = 0
	return (x + y) % spot == 0
		