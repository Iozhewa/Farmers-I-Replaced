from movement import goto, run, l_shape, diagonal

def miller(quota):
	while num_items(Items.Hay) < quota:
		run("hay")
		run("hay", l_shape)
		run("hay", diagonal)

if __name__ == "__main__":
	do_a_flip()
	
	goto()
	miller(4*10**4)
	
	pet_the_piggy()