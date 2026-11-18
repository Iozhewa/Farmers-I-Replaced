from movement import goto, run, l_shape, diagonal
from accountant import account, declare

def pumper(quota):
	while num_items(Items.Pumpkin) < quota:
		if num_items(Items.Carrot) < 10**4:
			if num_items(Items.Power) < 100:
				declare("Charged carrot mode.")
				run("bush_carrots", l_shape)
			else:
				quick_print("Charging carrot mode.")
				run("sun_carrots", diagonal)
		elif num_items(Items.Power) > 300:
			declare("Charged pumpkin mode.")
			run("bush_pumpkins", l_shape)
		else:
			declare("Charging pumpkin mode.")
			run("sun_pumpkins")
		account()
		quick_print("---")

if __name__ == "__main__":
	change_hat(Hats.Pumpkin_Hat)
	do_a_flip()
	
	goto()
	pumper(8*10**5)
	
	pet_the_piggy()