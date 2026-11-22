from movement import *
from setups import *

def coal():
	if get_ground_type() == Grounds.Coal:
		dig()

# recommended metQuota: num_items(Grounds.Coal) >= 100
def farm_coal(fromTheTop=False, metQuota=True):
	if fromTheTop:
		clear()
	goto()
	bounds = (5, 10)
	while get_stability() < 2 or not(metQuota):
		for x in range(get_world_size()-1):
			if x % 2 == 0:
				goto(x, bounds[0])
			else:
				goto(x, bounds[1])
			for _ in range(2):
				if get_ground_type() == Grounds.Coal:
					change_hat(Hats.Coal_Hat)
					cycle(coal)
				dig()
