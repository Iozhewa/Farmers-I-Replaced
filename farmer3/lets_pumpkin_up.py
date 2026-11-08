from movement import goto, run, l_shape, diagonal

def pumper(quota):
	while num_items(Items.Pumpkin) < quota:
		if num_items(Items.Carrot) < 10**4:
			if num_items(Items.Power) < 100:
				run("bush_carrots", l_shape)
			else:
				run("sun_carrots", diagonal)
		elif num_items(Items.Power) > 300:
			run("bush_pumpkins", l_shape)
		else:
			run("sun_pumpkins")

if __name__ == "__main__":
	do_a_flip()
	
	goto()
	pumper(8*10**5)
	
	pet_the_piggy()