do_a_flip()
while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(South)
while num_items(Items.Wood) < 100:
	for _ in range(get_world_size()):
		move(North)
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Bush)
	move(East)
pet_the_piggy()