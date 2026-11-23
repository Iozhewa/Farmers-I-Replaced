from setups import *
from movement import *

def weird():
	collect()
	plant(Entities.Tree)
	while not(can_harvest()):
		use_item(Items.Fertilizer)
	harvest()
	
if __name__ == "__main__":
	do_a_flip()
	
	goto()
	cycle(weird)
	
	pet_the_piggy()