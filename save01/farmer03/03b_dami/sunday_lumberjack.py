from movement import goto, run, diagonal, l_shape
from accountant import account, declare

def lumber(quota):
	while num_items(Items.Wood) < quota:
		if num_items(Items.Carrot) < 10**4:
			if num_items(Items.Power) < 100:
				declare("Charged carrot mode.")
				run("bush_carrots", l_shape)
			else:
				declare("Charging carrot mode.")
				run("sun_carrots", diagonal)
		elif num_items(Items.Power) > 300:
			declare("Charged tree mode.")
			run("bush_trees", diagonal)
		else:
			declare("Charging tree mode.")
			run("sun_trees", l_shape)			
		account()
		quick_print("---")

if __name__ == "__main__":
	change_hat(Hats.Tree_Hat)
	do_a_flip()
	
	goto()
	lumber(4*10**5)

	pet_the_piggy()