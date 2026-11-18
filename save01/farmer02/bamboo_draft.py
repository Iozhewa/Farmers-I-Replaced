from movement import goto, work_shift
def panda_run():
	pass
#work_shift("plow")
lane = get_world_size()-1
goto(0,0)
hover(0)
goto(0, lane)
goto(0,0)
stalks = []
for _ in range(lane):
	move(North)
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Bamboo)
	stalks.append(measure())
move(East)
move(North)
	
def watch(start=0, end=0):
	while get_time()-start < end:
		continue

modifier = 0
while min(stalks) < 18:
	if max(stalks) - modifier < 1:
		break
	watch(get_time(), max(stalks) - modifier)
	modifier = max(stalks)
	index = 0
	for height in stalks:
		move(North)
		hover(height)
		move(West)
		stalks[index] = measure()
		move(East)
		index += 1
	goto(1,0)
goto(0,0)
hover(0)
goto(0, lane)
goto(0,0)
pet_the_piggy()