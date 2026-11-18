from movement import goto, run, l_shape
from accountant import account, declare

def tiller(quota):
	while num_items(Items.Carrot) < quota:
		if num_items(Items.Wood) < 10**4:
			if num_items(Items.Power) < 100:
				declare("Charged tree mode.")
				run("bush_trees", l_shape)
			else:
				quick_print("Charging tree mode.")
				run("sun_trees")
		elif num_items(Items.Power) > 300:
			declare("Charged carrot mode.")
			run("bush_carrots")
		elif num_items(Items.Hay) < 4*10**4:
			declare("Hay mode.")
			run("hay")
		else:
			declare("Charging carrot mode.")
			run("sun_carrots", l_shape)
		account()
		quick_print("---")

if __name__ == "__main__":
	change_hat(Hats.Carrot_Hat)
	do_a_flip()
	
	goto()
	tiller(4*10**5)
	
	pet_the_piggy()