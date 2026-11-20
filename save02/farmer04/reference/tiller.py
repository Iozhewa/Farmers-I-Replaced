for _ in range(get_world_size()):
	for _ in range(get_world_size()):
		move(North)
		if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
			harvest()			
		if get_ground_type() != Grounds.Soil:
			till()
	move(East)