from movement import *

def reset(pure=False):
	if pure:
		clear()
	change_hat(Hats.Sunflower_Hat)
	pet_the_piggy()
	goto(0, 0)
	do_a_flip()

def poly_collect():
	lane = get_world_size()-1
	x, y = coord()
	run("poly")
	goto(x, y)
	run("collect")

def packUp(pure=False):
	for _ in range(6):
		if pure:
			run("raze")
		else:
			run("collect")

def findCoal():
	pet_the_piggy()
	clear()
	goto(0, 0)
	do_a_flip()
	packUp(True)
	goto(5, 5)
	while get_ground_type() != Grounds.Clay:
		for _ in range(2):
			dig()
		run("coal")

def reduceClay():
	initial = 0
	final = 0
	while final - initial < 9:
		initial = get_time()
		run("rice")
		final = get_time()
		quick_print(final - initial)
		
def rock_hard():
	findCoal()
	reduceClay()
	for _ in range(6):
		run("collect")