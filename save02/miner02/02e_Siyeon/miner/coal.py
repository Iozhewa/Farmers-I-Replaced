from movement import *
from setups import *

def coal():
	if get_ground_type() == Grounds.Coal:
		dig()

def farm_coal(fromTheTop=False):
	if fromTheTop:
		clear()
	goto()
	bounds = (5, 10)
	while True:
		for x in range(get_world_size()-1):
			if x % 2 == 0:
				goto(x, bounds[0])
			else:
				goto(x, bounds[1])
			for _ in range(2):
				if get_ground_type() == Grounds.Coal:
					change_hat(Hats.Coal_Hat)
					cycle(coal)
				if get_stability() > 2:
					return  # Experimental
				dig()
