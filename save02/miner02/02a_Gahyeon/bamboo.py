from setups import *
from movement import *
from sunflowers import farm_sunflower

goto()
heights = []
for _ in range(get_world_size()):
	move(North)
	plow()
	plant(Entities.Bamboo)
	heights.append(measure())
move(East)

start = get_time()
elapsed = get_time() - start
while elapsed < max(heights):
	for _ in range(get_world_size()):
		move(North)
		collect()
		plow()
		plant(Entities.Carrot)
		water()
	elapsed = get_time() - start

goto()
refresh = []
for height in heights:
	move(North)
	hover(height)
	move(East)
	refresh = measure()
	move(West)

goto(1, 0)