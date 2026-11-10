from scenarios import *

def process(query):
	if query == "simple":
		return
	elif query == "collect":
		collect()
	elif query == "plow":
		plow()
	elif query == "hay":
		hay()
	elif query == "bush_carrots":
		carrots()
	elif query == "sun_carrots":
		carrots(True)
	elif query == "bush_trees":
		trees()
	elif query == "sun_trees":
		trees(True)	
	elif query == "bush_pumpkins":
		pumpkins()
	elif query == "sun_pumpkins":
		pumpkins(True)
	elif query == "bush_bamboo":
		bamboo()
	elif query == "sun_bamboo":
		bamboo(True)
	elif query == "coal_fast":
		coal()
	elif query == "coal_charge":
		coal(True)
	elif query == "rice_fast":
		rice()
	elif query == "rice_charge":
		rice(True)
	elif query == "prospect":
		prospect()
	elif query == "weird":
		return
		weird()  # TODO
	elif query == "cactus":
		return
		cactus()  # TODO
	else:
		print("Unknown request!")
		break  # Crude, I know

