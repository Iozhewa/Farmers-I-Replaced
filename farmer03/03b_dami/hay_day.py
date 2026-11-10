from movement import goto, run, l_shape, diagonal
from accountant import account

def miller(quota):
	while num_items(Items.Hay) < quota:
		run("hay")
		run("hay", l_shape)
		run("hay", diagonal)
		
		account()
		quick_print("---")

if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	do_a_flip()
	
	goto()
	miller(4*10**4)
	
	pet_the_piggy()