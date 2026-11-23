def trivial_solution():
	harvest()

cycle = {North: East, East: South,
		South: West, West: North}
invert = {North: West, West: South,
		South: East, East: North}
def left_hand_rule():
	direction = North
	while True:
		while not(can_move(cycle[direction])):
			direction = cycle[direction]
		move(cycle[direction])
		direction = invert[direction]
		if get_entity_type() == Entities.Treasure:
			harvest()
			return
		if get_entity_type() != Entities.Hedge:
			return

def right_hand_agents():
	direction = North
	counter = 0
	strategy = right_hand_agents
	toggle = {right_hand_agents:left_hand_rule,
		left_hand_rule:right_hand_agents}
	while True:
		while not(can_move(invert[direction])):
			direction = invert[direction]
		move(invert[direction])
		direction = cycle[direction]
		if get_entity_type() == Entities.Treasure:
			harvest()
			return
		if get_entity_type() != Entities.Hedge:
			return
		quick_print(counter)
		if counter % 11 == 0 and num_drones() != max_drones():
			spawn_drone(toggle[strategy])
			strategy = toggle[strategy]
		else:
			counter += 1
