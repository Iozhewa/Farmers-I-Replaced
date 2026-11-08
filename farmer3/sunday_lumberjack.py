from movement import goto, run, diagonal, l_shape

def lumber(quota):
	while num_items(Items.Wood) < quota:
		if num_items(Items.Carrot) < 10**4:
			if num_items(Items.Power) < 100:
				run("bush_carrots", l_shape)
			else:
				run("sun_carrots", diagonal)
		elif num_items(Items.Power) > 300:
			run("bush_trees", diagonal)
		else:
			run("sun_trees", l_shape)

if __name__ == "__main__":
	do_a_flip()
	
	goto()
	lumber(4*10**5)

	pet_the_piggy()