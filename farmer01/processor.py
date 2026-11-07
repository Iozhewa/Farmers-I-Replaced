from logic import *

def process(request, spec=6):
	if request == "collect":
		change_hat(Hats.Purple_Hat)
		harvest()
	elif request == "simple":
		change_hat(Hats.Straw_Hat)
		return
	elif request == "charged":
		change_hat(Hats.Sunflower_Hat)
		charged(spec)
	elif request == "poly":
		change_hat(Hats.Wizard_Hat)
		poly()
	elif request == "bushed":
		change_hat(Hats.Tree_Hat)
		bushed(spec)
	elif request == "raze":
		change_hat(Hats.Carrot_Hat)
		raze()
	elif request == "rice":
		change_hat(Hats.Rice_Hat)
		rice()
	elif request == "coal":
		change_hat(Hats.Mining_Hat)
		coal()
	else:
		change_hat(Hats.Traffic_Cone)
		print("???")