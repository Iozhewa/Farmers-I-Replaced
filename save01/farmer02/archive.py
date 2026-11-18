from movement import *
def sequence_digger(focus="iron", pure=False, quota=15):
	if pure:
		clear()
	work_shift("plow")
	mole_run()
	if focus == "coal":
		return
	carabao_run()
	if focus == "rice":
		return
	golem_run()	

def get_carrots(amount=10**3):
	while num_items(Items.Carrot) < amount:
		if num_items(Items.Power) > 1:
			work_shift("carrot")
		else:
			work_shift("carrot_charge")

def get_wood(amount=10**3):
	while num_items(Items.Wood) < amount:
		if num_items(Items.Power) > 1:
			work_shift("tree")
		elif num_items(Items.Carrot) < 10**3:
			work_shift("carrot")
		else:
			work_shift("tree_charge")