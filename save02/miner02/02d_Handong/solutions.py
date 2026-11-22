def trivial_solution():
	harvest()

cycle = {North: East, East: South,
		South: West, West: North}
invert = {North: West, West: South,
		South: East, East: North}
def left_hand_rule():
	change_hat(Hats.Gold_Hat)
	direction = North
	while True:
		while not(can_move(cycle[direction])):
			direction = cycle[direction]
		move(cycle[direction])
		direction = invert[direction]
		if get_entity_type() == Entities.Treasure:
			harvest()
			return

if __name__ == "__main__":
	left_hand_rule()  
	# Attempting to break