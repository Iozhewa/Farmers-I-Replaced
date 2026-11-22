from movement import *
from setups import *

def clayDig():
	while get_ground_type() != Grounds.Clay:
		if get_ground_type() == Grounds.Rock:
			break
		dig()

def rice():
	collect()
	if get_ground_type() == Grounds.Dry_Rice_Terrace:
		dig()
	plant(Entities.Rice)

def farm_rice(fromTheTop=False):
	if fromTheTop:
		clear()
	goto()
	cycle(clayDig)
	while True:
		if get_ground_type() == Grounds.Rock:
			cycle(collect)
			break
		else:
			change_hat(Hats.Rice_Hat)
			cycle(rice)
		dig()