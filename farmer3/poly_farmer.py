from movement import goto, run

lane = get_world_size()-1
stalks = []

def setup_bamboo():
	goto(0,0)
	hover(0)
	goto(0, lane)
	goto(0,0)
	for _ in range(lane):
		move(North)
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Bamboo)
		stalks.append(measure())
	move(East)
	move(North)
	
def poly_wait(start=0, end=0):
	goto(1, 0)
	if get_ground_type() != Grounds.Grassland:
		till()
	while get_time()-start < end:
		preference = get_companion()
		if preference == None:
			harvest()
			move(North)
			continue
			
		companion, (x, y) = preference
		if x == 0:  # Don't touch the bamboo
			harvest()
			move(North)
			continue
			
		ox, oy = (get_pos_x(), get_pos_y())
		goto(x,y)
		if can_harvest():
			harvest()
		
		ground = get_ground_type()	
		if companion == Entities.Carrot and ground == Grounds.Grassland:
			till()
			plant(companion)
		if companion != Entities.Carrot and ground == Grounds.Soil:
			till()
			plant(companion)
		goto(ox, oy)
		harvest()

def cleanup_bamboo():
	goto(0,0)
	hover(0)
	goto(0, lane)
	goto(0,0)

def poly_farm(quota):
	while num_items(Items.Bamboo) < quota:
		setup_bamboo()
	
		modifier = 0
		while min(stalks) < 18:
			if max(stalks) - modifier < 1:
				break
			poly_wait(get_time(), max(stalks) - modifier)
			goto(1, 0)
			modifier = max(stalks)
			index = 0
			for height in stalks:
				move(North)
				if get_pos_y() == 0:
					move(North)
				hover(height)
				move(West)
				stalks[index] = measure()
				move(East)
				index += 1
			goto(1,0)
		cleanup_bamboo()
		global stalks
		stalks = []

if __name__ == "__main__":
	gains = {}
	gains["Hay"] = num_items(Items.Hay)
	gains["Wood"] = num_items(Items.Wood)
	gains["Bamboo"] = num_items(Items.Bamboo)
	
	do_a_flip()
	clear()
	poly_farm(2*10**5)
	
	gains["Hay"] = num_items(Items.Hay) - gains["Hay"]
	gains["Wood"] = num_items(Items.Wood) - gains["Wood"]
	gains["Bamboo"] = num_items(Items.Bamboo) - gains["Bamboo"]
	for gain in gains:
		quick_print(gain, ":", gains[gain])
	run("plow")
	pet_the_piggy()