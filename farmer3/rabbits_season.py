from movement import goto, run, l_shape

def tiller(quota):
	while num_items(Items.Carrot) < quota:
		if num_items(Items.Wood) < 10**4:
			if num_items(Items.Power) < 100:
				run("bush_trees", l_shape)
			else:
				run("sun_trees")
		elif num_items(Items.Power) > 300:
			run("bush_carrots")
		elif num_items(Items.Hay) < 4*10**4:
			run("hay")
		else:
			run("sun_carrots", l_shape)

if __name__ == "__main__":
	do_a_flip()
	
	goto()
	tiller(4*10**5)
	
	pet_the_piggy()