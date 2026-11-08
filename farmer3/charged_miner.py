from movement import goto, run, diagonal

def resurface(pure=False):
	if pure:
		clear()
	run("plow", diagonal)

def toClay():
	goto()
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

def toRock():
	goto()
	while get_ground_type() != Grounds.Rock:
		if get_pos_z() % 2 == 0:
			run("rice_charge")
		else:
			run("rice_fast")
	for _ in range(3):
		run("rice_fast")

def toIron():
	while get_ground_type != Grounds.Quartz:
		prospect = prospect_iron()
		if prospect != None:
			move(prospect)
		else:
			dig()
		dig()

def toQuartz():
	pass  # Add jump() onto toIron() first?

if __name__ == "__main__":
	goto()
	do_a_flip()
	
	resurface(True)
	toClay()
	toRock()
	toIron()
	
	pet_the_piggy()