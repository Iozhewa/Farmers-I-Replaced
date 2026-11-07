from logic import *

def process(request):
	if request == "simple":
		return
	elif request == "collect":
		collect()
	elif request == "plow":
		plow()
	elif request == "carrot":
		carrot()
	elif request == "carrot_charge":
		carrot(True)
	elif request == "tree":
		tree()
	elif request == "tree_charge":
		tree(True)
	elif request == "pumpkin":
		pumpkin()
	elif request == "pumpkin_charge":
		pumpkin(True)	
	elif request == "coal":
		coal()
	elif request == "rice":
		rice()
	elif request == "iron":
		iron()
	else:
		print("Request unknown!")
		break  # Crude breakpoint