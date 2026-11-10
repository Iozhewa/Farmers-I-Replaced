book = {}
for item in Items:
	book[item] = num_items(item)

def account():
	for item in Items:
		delta = num_items(item) - book[item]
		if delta > 0:
			quick_print(item, "gained:", delta)
		elif delta < 0:
			quick_print(item, "lost:", delta)

def declare(mode):
	if mode == "Charged carrot mode.":
		change_hat(Hats.Carrot_Hat)
	elif mode == "Charged bush mode.":
		change_hat(Hats.Wizard_Hat)
	elif mode == "Charged pumpkin mode.":
		change_hat(Hats.Pumpkin_Hat)
	else:
		change_hat(Hats.Sunflower_Hat)
	quick_print(mode)

for _ in range(5):
	quick_print(".")