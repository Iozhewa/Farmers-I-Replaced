from movement import goto, run, l_shape
from accountant import account

def resurface(pure=False):
	goto()
	change_hat(Hats.Traffic_Cone)
	if pure:
		clear()
	run("plow", l_shape)

def toClay():
	goto()
	change_hat(Hats.Coal_Hat)
	while get_ground_type() != Grounds.Clay:
		if get_pos_z() % 4 == 0:
			run("coal_charge")
		else:
			run("coal_fast")
		for i in range(get_world_size()):
			goto(i, i)
			if can_harvest():
				harvest()
			dig()
			dig()
		account()
		quick_print("---")

def toRock():
	goto()
	change_hat(Hats.Rice_Hat)
	while get_ground_type() != Grounds.Rock:
		if get_pos_z() % 2 == 0:
			run("rice_charge")
		else:
			run("rice_fast")
		account()
		quick_print("---")
		
	for _ in range(3):
		run("rice_fast")
		account()
		quick_print("---")
	
	run("collect")
	account()
	quick_print("---")

def toIron():
	goto()
	change_hat(Hats.Bucket)
	while get_ground_type() != Grounds.Quartz:
		prospect = prospect_iron()
		if prospect != None:
			move(prospect)
		else:
			dig()
		dig()
		
		account()
		quick_print("---")

def toQuartz():
	goto()
	change_hat(Hats.Mining_Hat)
	i = 0
	while get_ground_type() not in {Grounds.Sand, Grounds.Limestone}:
		if i % 4 == 0 or i % 5 == 0:
			run("prospect")
		
		prospect = prospect_iron()
		if prospect != None:
			move(prospect)
		else:
			dig()
		dig()
		i += 1
		
		account()
		quick_print("---")

if __name__ == "__main__":
	do_a_flip()
	
	resurface(True)
	toClay()
	pet_the_piggy()
	
	toRock()
	pet_the_piggy()
	
	toIron()
	pet_the_piggy()
	
	toQuartz()
	pet_the_piggy()