# Farmers I Replaced
Imagine liking a game so much you blog about it...


__Table of Contents__
1. [Bulding Blocks (Singular Code)](#building-blocks)
2. [Delegations (First Modules)](#delegations)
3. [Sunflowers and Pumpkins](#sunflowers-and-pumpkins)
4. [Polyculture](#polyculture)
5. [Descending (Mining)](#descending)
6. [Prospecting](#prospecting)

## Building Blocks
See [farmer01](save02\farmer01) for the chapter package.

__Hat__: Straw
### Unlocking `while`
No loops, no recursions here. Just a gross amount of duplicated code :]
``` python
do_a_flip()
harvest()
harvest()
harvest()
harvest()
harvest()  # just getting 5 wheat
```
### Unlocking `speed (I)`
A loop without conditional statements is a donut without icing nor glaze
``` python
do_a_flip()
while True: # No conditions unlocked yet...
    harvest()
pet_the_piggy() 
```
### Unlocking `expand (I)`, `plant`
Something new to ponder: What can be faster if you ask the drone to consider it?
``` python
do_a_flip()
while True:
	if can_harvest():
		harvest()
pet_the_piggy()
```
---
__Hat__: Brown
### Unlocking `speed (II)` and `expand (II)`
A program taking in both wood and hay! Perhaps the crop ratio will matter later on...
``` python
do_a_flip()
while True:
	move(North)
	if can_harvest():
		harvest()
	plant(Entities.Bush)
pet_the_piggy()
```
### Unlocking `carrots (I)` and `watering (I)`
Motivation for the `for` loop! With my favorite wildcard, no less.
``` python
do_a_flip()
while True:
	for _ in range(get_world_size()):
		move(North)
		if can_harvest():
			harvest()
		plant(Entities.Bush)
	move(East)
pet_the_piggy()
```
### Unlocking `print()`, `operators`, and `senses`
Cheeky submission, opening the door to future Template patterns
``` python
do_a_flip()
while True:
	for _ in range(get_world_size()):
		move(North)
		if can_harvest():
			harvest()
		#plant(Entities.Bush)
	move(East)
pet_the_piggy()
```
### Unlocking `variables` and `functions`
Some reset code has arrived! Along with conditions on the program's main loop.
``` python
do_a_flip()
while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(South)
while num_items(Items.Carrot) < 50:
	for _ in range(get_world_size()):
		move(North)
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		if num_items(Items.Water) > 0 and get_water() < 0.5:
			use_item(Items.Water)
	move(East)
pet_the_piggy()
```
---
## Delegations
At this point, the same bit of code needs just a few tweaks to focus on Hay, Wood, and Carrots. We can get a `Main` program to access `CarrotFarmer`, `BushFarmer`, `HayFarmer`, of some `Farmer` abstraction.

Well, this much abstraction would be great with Object-Oriented Programming. But if _The Farmer Was Replaced_ is anything, it's restrictive. See [farmer02](save02\farmer02) for the chapter package.

### Unlocking `expand (III)`
__main__
Refer to [02a_gahyeon]() (link tba) for full package
``` python
from movement import goto
from hay import farm_hay
from bushes import farm_bush
from carrots import farm_carrot

do_a_flip()

goto(0, 0)
farm_bush(100)
farm_carrot(50)

pet_the_piggy()
```
### Unlocking `speed (III)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_bush(80)  # Playing with (hay) + (wood) -> (carrot)
farm_carrot(50)

pet_the_piggy()
```
### Unlocking `trees (I)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
#farm_hay(80)
#farm_bush(80)
farm_carrot(80)  # Utilizing the 1:1:1 ratio for 30 banked crop, each

pet_the_piggy()
```
### Unlocking `watering (II)`
__main__
``` python
from movement import goto
from hay import farm_hay
from bushes import farm_bush
from carrots import farm_carrot
from trees import farm_tree

do_a_flip()

goto(0, 0)
#farm_hay(80)
#farm_bush(80)
#farm_carrot(80)
farm_tree(200)

pet_the_piggy()
```
### Unlocking `expand (IV)`
__main__
``` python
...

do_a_flip()

# 100 wood, 50 carrot
# 130 wood, 80 carrot
goto(0, 0)
farm_hay(80)
farm_bush(30)
farm_carrot(80)
farm_tree(100)

pet_the_piggy()
```
### Unlocking `grass (II)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_hay(360)

pet_the_piggy()
```
### Unlocking `carrots (II)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_tree(200)  # Good test of overflow
farm_bush(280)

pet_the_piggy()
```
### Unlocking `grass (III)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_tree(400)  # Good test of overflow
farm_bush(580)

pet_the_piggy()
```
### Unlocking `trees (II)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_hay(380)

pet_the_piggy()
```
### Unlocking `speed (IV)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_hay(580)
farm_tree(400)
farm_bush(580)
farm_carrot(580)

pet_the_piggy()
```
### Final speed upgrade! `speed (v)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_hay(1080)
farm_tree(850)
farm_bush(1080)
farm_carrot(1080)

pet_the_piggy()
```
### Unlocking `sunflower (I)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_hay(580)
farm_tree(400)
farm_bush(580)
farm_carrot(580)

pet_the_piggy()
```
### Unlocking `lists`
__main__
``` python
...

do_a_flip()

goto(0, 0)
farm_hay(580)
farm_tree(400)
farm_bush(580)
farm_carrot(580)

pet_the_piggy()
```
---
## Sunflowers and Pumpkins
See [farmer03](save02\farmer03) for the chapter package.

### Unlocking `trees (III)`
__main__
``` python
from movement import goto
from hay import farm_hay
from bushes import farm_bush
from carrots import farm_carrot
from trees import farm_tree
from sunflower import farm_sunflower

do_a_flip()

goto()
farm_tree(1300)
farm_carrot(1300)
farm_sunflower(1300)
farm_hay(1300)

pet_the_piggy()
```
### Unlocking `carrots (III)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(1300)
farm_carrot(1300)
farm_sunflower(1300)
farm_bush(1300)

pet_the_piggy()
```
### Unlocking `watering (III)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(880)

pet_the_piggy()
```
### Unlocking `fertilizer (IV)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(2400)
farm_bush(2580)

pet_the_piggy()
```
### Unlocking `trees (IV)`
__main__
``` python
...

do_a_flip()

goto()
farm_hay(4880)

pet_the_piggy()
```
### Unlocking `carrots (IV)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(6000)
farm_bush(6300)

pet_the_piggy()
```
### Unlocking `watering (IV)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(3000)
farm_bush(3300)

pet_the_piggy()
```
### Unlocking `watering (V)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(10000)
farm_bush(13000)

pet_the_piggy()
```
### Unlocking `trees (V)`
__main__
``` python
...

do_a_flip()

goto()
farm_hay(2*10**4)

pet_the_piggy()
```
### Unlocking `grass (IV)`, `fertilizer (I)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(10**4)
farm_bush(1.3*10**4)

pet_the_piggy()
```
### Unlocking `fertilizer (II)`, `fertilizer (III)`
__main__
``` python
...

do_a_flip()

goto()
farm_tree(10**3)
farm_bush(1600)

pet_the_piggy()
```

_later_

__main__
``` python
do_a_flip()

goto()
farm_tree(9000)
farm_bush(10**4)

pet_the_piggy()
```

### Unlocking `pumpkins (I)`, `pumpkins (II)`, `pumpkins (III)`, `pumpkins (IV)`
__main__
``` python
...

do_a_flip()

goto()
farm_carrot(1000)
farm_sunflower(100)  # Charging on the side

pet_the_piggy()
```
_later_

__main__
``` python
...

do_a_flip()

goto()
farm_carrot(1300)

pet_the_piggy()
```
_later_

__main__
``` python
...

do_a_flip()

goto()
farm_hay(4300)
farm_tree(4000)
farm_bush(4300)
farm_carrot(4300)

pet_the_piggy()
```
_later_

__main__
``` python
...

do_a_flip()

goto()  # Note whenever power ran out, all you need is to reboot main and get 100 power
farm_sunflower(100)
farm_hay(16*10**3)  # This is ignored if the quota is satisfied
farm_tree(10**4)
farm_bush(16*10**3)
farm_carrot(16*10**3)

pet_the_piggy()
```

### Unlocking `expand (V)`, `utilities`, `timing`
__main__
``` python
from movement import goto
from hay import farm_hay
from bushes import farm_bush
from carrots import farm_carrot
from trees import farm_tree
from sunflowers import farm_sunflower
from pumpkins import farm_pumpkin

do_a_flip()

goto()
farm_hay(9000)
farm_tree(9000)
farm_carrot(100)  
farm_sunflower(100) # 1 carrot = 1 sunflower
farm_carrot(9000) # 1 hay + 1 wood = 1 carrot
farm_pumpkin(1100) # 8 carrot = 1 pumpkin

pet_the_piggy()
```

### Unlocking `polyculture`
__main__
``` python
...

do_a_flip()

goto()
farm_hay(2*10**4)
farm_tree(2*10**4)
farm_carrot(200)
farm_sunflower(200)
farm_carrot(2*10**4)
farm_pumpkin(2.5*10**3)

pet_the_piggy()
```
## Interlude, leading to Polyculture
### Unlocking `dictionaries`
__main__
``` python
...

do_a_flip()

goto()
farm_pumpkin(2.5*10**3)

pet_the_piggy()
```
### Unlocking `cactus (I)`
__main__
``` python
...

do_a_flip()

goto()
farm_pumpkin(5*10**3)

pet_the_piggy()
```
### Unlocking `costs`
__main__
``` python
...

do_a_flip()

goto()
farm_pumpkin(2.5*10**3)

pet_the_piggy()
```
### Unlocking `auto-unlock`
__main__
``` python
...


do_a_flip()

goto()
farm_pumpkin(5*10**3)

pet_the_piggy()
```
### Unlocking `expand (VI)`
__main__
``` python
...


do_a_flip()

goto()
farm_carrot(200)
farm_sunflower(200)  # Charging
farm_hay(2.4*10**4)
farm_tree(2*10**4)
farm_bush(400)
farm_carrot(2.4*10**4)  # Supplying
farm_pumpkin(8*10**3)  # Farming

pet_the_piggy()
```
## Polyculture

(`carrots (V)` was unlocked during experiments)<br>
(`watering (VI)` was unlocked during experiments)

### Final Fertilizer Upgrade!
__main__
``` python
from movement import goto, rotation
from setups import *
from poly import poly_farm

do_a_flip()

goto(0, 0)
cycle(deplow)
while num_items(Items.Wood) < 5.4*10**4:
	poly_farm(Entities.Bush)
	cycle(collect)

pet_the_piggy()
```
### Unlocking `pumpkins (V)`
__main__
``` python
from movement import goto, rotation
from setups import *
from poly import poly_farm
from sunflowers import farm_sunflower
from pumpkins import farm_pumpkin

do_a_flip()

goto(0, 0)
cycle(collect)
farm_sunflower()
while num_items(Items.Carrot) < 7*10**4:
	poly_farm(Entities.Carrot, 7*10**4)

pet_the_piggy()
```
### Unlocking `cactus (II)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
cycle(collect)
while num_items(Items.Pumpkin) < 2.1*10**4:
	if num_items(Items.Carrot) < 5*10**3:
		poly_farm(Entities.Carrot, 10**4)
	if num_items(Items.Power) < 1:
		farm_sunflower()
	farm_pumpkin(num_items(Items.Pumpkin)+100)

pet_the_piggy()
```
### Unlocking `expand (VII)`, `grass (V)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
cycle(collect)
while num_items(Items.Pumpkin) < 6.4*10**4:
	if num_items(Items.Power) < 1:
		farm_sunflower()
	if num_items(Items.Carrot) < 5*10**3:
		poly_farm(Entities.Carrot, 10**4)
	farm_pumpkin(num_items(Items.Pumpkin)+100)

pet_the_piggy()
```
### Unlocking `trees (VI)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
cycle(collect)
while num_items(Items.Hay) < 8*10**4:
	poly_farm(Entities.Grass, 8*10**4)

	if num_items(Items.Power) < 1:
		farm_sunflower()
	if num_items(Items.Carrot) < 5*10**3:
		poly_farm(Entities.Carrot, 10**4)

pet_the_piggy()
```
## Descending
(`mining (I)` was unlocked during experiments)

### Unlocking `mining (II)`
__main__
``` python
from movement import *
from setups import *

def powerset_2(a, b):
	result = []
	for x in (a, b):
		for y in (a, b):
			spot = (x, y)
			result.append(spot)
	return result

do_a_flip()

goto()
clear()
for i in range(5, 7):
	corner_set = powerset_2(i, get_world_size()-i)
	for coord in corner_set:
		print(coord)
		goto(coord[0], coord[1])
		for _ in range(0, 3):
			dig()

pet_the_piggy()
```
### Unlocking `Underground Senses`, `coal (I)`
__main__
``` python
...

do_a_flip()

while num_items(Items.Block) < 50:
	goto()
	clear()
	for i in range(1, 8):
		corner_set = powerset_2(i, get_world_size()-i)
		for coord in corner_set:
			goto(coord[0], coord[1])
			for _ in range(0, 3):
				dig()

pet_the_piggy()
```
### Unlocking `iron (I)`, `rice (I)`
__main__
``` python
...

do_a_flip()

while num_items(Items.Block) < 50:
	goto()
	clear()
	for i in range(2, 8):
		corner_set = powerset_2(i, get_world_size()-i)
		for coord in corner_set:
			goto(coord[0], coord[1])
			for _ in range(0, 3):
				dig()
		cycle(coal)

pet_the_piggy()
```
### Unlocking `Iron Prospcting`, `rice (II)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
clear()
dig_block()
dig_coal()
#farm_rice()

pet_the_piggy()
```
## Prospecting
### Unlocking `mining (III)`, `coal (II)`, `rice (III)`, `bamboo (I)`, `bamboo (II)`, `petrified pumpkins (I)`, 
__main__
``` python
from movement import goto, rotation
from setups import *
from poly import poly_farm
from sunflowers import farm_sunflower
from pumpkins import farm_pumpkin
from mining import *

do_a_flip()

goto(0, 0)
clear()
dig_block()
dig_coal()
farm_rice()
dig_iron(False)

pet_the_piggy()
```
### Unlocking `mining (IV)`, `coal (III)`, `rice (IV)`
__main__
``` python
...

do_a_flip()

goto(0, 0)
clear()
dig_block()
dig_coal()
farm_rice()
dig_iron()

pet_the_piggy()
```
## Interlude, modularizing mining code
(`jump` was unlocked during experiments)
### Unlocking `iron (II)`, `rice (VI)`
__main__
``` python
from coal import farm_coal

do_a_flip()

change_hat(Hats.Coal_Hat)
farm_coal()

pet_the_piggy()
```
### Unlocking `rice (VI)`, `bamboo (III)`, `Special Soils`
(`mining (V)`, `Colorful Blocks` was unlocked during experiments)

__main__
``` python
from rice import farm_rice

do_a_flip()

change_hat(Hats.Rice_Hat)
farm_rice()

pet_the_piggy()
```
### Unlocking `iron (III)`
__main__
``` python
do_a_flip()

change_hat(Hats.Coal_Hat)
farm_coal(True)

pet_the_piggy()
```
### Unlocking `petrified pumpkins (II)`
__main__
``` python
from setups import *
from movement import *
from coal import farm_coal
from rice import farm_rice
from iron import farm_iron

do_a_flip()

change_hat(Hats.Bucket)
farm_iron(True)

pet_the_piggy()
```
### Unlocking `quartz (I)`
__main__
``` python
from setups import *
from movement import *
from coal import farm_coal
from rice import farm_rice
from iron import farm_iron

do_a_flip()

farm_coal(True)
farm_iron()

pet_the_piggy()
```
### Unlocking `mining (VII)`
__main__
``` python
...

do_a_flip()

predicate = num_items(Items.Coal) >= 100
while num_items(Items.Iron) < 70:
	farm_coal(True, predicate)
	farm_iron(False, 70)
	clear()

pet_the_piggy()
```
### Unlocking `quartz (II)`
__main__
``` python
...

do_a_flip()

# had to manually adjust this
predicate = num_items(Items.Coal) >= 100
while num_items(Items.Iron) < 200:
	farm_iron(False, 200)
	farm_coal(True, predicate)
	#clear()

pet_the_piggy()
```
### Unlocking `pyramids (I)`
__bamboo__
``` python
from setups import *
from movement import *

heights = []
def plant_bamboo():
	goto()
	for _ in range(get_world_size()):
		move(North)
		plow()
		plant(Entities.Bamboo)
		heights.append(measure())
	move(East)

def watch_bamboo():
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

def trim_bamboo():
	goto(1, 0)
	refresh = []
	for height in heights:
		move(North)
		hover(height)
		move(West)
		refresh.append(measure())
		move(East)
	global heights
	heights = refresh
	goto(1, 0)

def reset_bamboo():
	endpoint = get_world_size() - 1
	goto(1, endpoint)
	hover(0)
	goto(0, endpoint)
	goto()

def farm_bamboo():
	plant_bamboo()
	while max(heights) < 18:
		watch_bamboo()
		trim_bamboo()
	reset_bamboo()
	
if __name__ == "__main__":
	reset_bamboo()
	#farm_bamboo()
```
### Unlocking `petrified pumpkins (III)`
__main__
``` python
from setups import *
from movement import *
from bamboo import farm_bamboo

do_a_flip()

while num_items(Items.Bamboo) < 4*10**4:
	farm_bamboo()

pet_the_piggy()
```
### Final Coal Upgrade! and Unlocking `rice (VII)`
__main__
``` python
from setups import *
from movement import *
from rice import farm_rice

do_a_flip()

while num_items(Items.Rice) < 2*10**4:
	goto()
	clear()
	farm_rice()

pet_the_piggy()
```
### Unlocking `treasure map (I)`, `treasure map (II)`
__main__
``` python
from setups import *
from movement import *
from bamboo import farm_bamboo, reset_bamboo

do_a_flip()

reset_bamboo()
while num_items(Items.Bamboo) < 4.5*10**4:
	farm_bamboo()

pet_the_piggy()
```
### Unlocking `quartz (III)`
__main__
``` python
from setups import *
from movement import *
from coal import farm_coal
from iron import farm_iron

do_a_flip()

while num_items(Items.Iron) < 400:
	farm_iron(400)
	clear()
	farm_coal()

pet_the_piggy()
```
### Final quartz upgrade! Unlocking `Ore Boost`
__main__
``` python
...

do_a_flip()

while num_items(Items.Iron) < 10**3:
	farm_iron(10**3)
	clear()
	farm_coal()

pet_the_piggy()
```
### Unlocking `mushroom (I)`, `treasure map (III)` and `treasure map (IV)`, `mining (VIII)`
__main__
``` python
from setups import *
from movement import *
from coal import farm_coal
from iron import farm_iron
from quartz import farm_quartz

do_a_flip()

while num_items(Items.Quartz) < 60:
	farm_quartz(60)
	if num_items(Items.Iron) < 1:
		farm_iron(100)
	if num_items(Items.Coal) < 1:
		clear()
		farm_coal()

pet_the_piggy()
```
### Unlocking `iron (IV)`
__main__
``` python
from setups import *
from movement import *
from coal import farm_coal

do_a_flip()

while num_items(Items.Coal) < 600:
	clear()
	farm_coal()

pet_the_piggy()
```
### Final treasure map upgrade!
__main__
``` python
from setups import *
from movement import *
from coal import farm_coal
from iron import farm_iron
from quartz import farm_quartz

do_a_flip()

while num_items(Items.Quartz) < 700:
	farm_quartz(700)
	if num_items(Items.Iron) < 1:
		farm_iron(100)
	if num_items(Items.Coal) < 1:
		clear()
		farm_coal()

pet_the_piggy()
```
### Unlocking `mazes (I)`
__main__
``` python
from setups import *
from movement import *

def weird():
	collect()
	plant(Entities.Tree)
	while not(can_harvest()):
		use_item(Items.Fertilizer)
	harvest()
	
if __name__ == "__main__":
	do_a_flip()
	
	goto()
	cycle(weird)
	
	pet_the_piggy()
```
### Unlocking `set_speed()`
__solutions__
``` python
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
```
### Unlocking `pyramids (II)`, `mushroom (II)`, 
__mazes__
``` python
from setups import *
from movement import *
from solutions import *

mid = get_world_size()/2
def setup(size=1):
	goto(mid, mid)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, size)

def farm_treasure(quota=5000):
	change_hat(Hats.Gold_Hat)
	counter = 1
	while num_items(Items.Gold) < quota:
		collect()
		setup(counter)
		if counter == 1:
			trivial_solution()
		else:
			left_hand_rule()
		if counter == get_world_size()-1:
			counter = 1
		else:
			counter += 1
```
### Unlocking `mushrooms (III)`
__main__
``` python
from setups import *
from movement import *
from mazes import farm_treasure

do_a_flip()

farm_treasure(3000)

pet_the_piggy()
```
### Unlocking `pyramids (III)`
__main__
``` python
from setups import *
from movement import *
from mazes import farm_treasure

do_a_flip()

farm_treasure(7000)

pet_the_piggy()
```
### Unlocking `Megafarm (I)`
__main__
``` python
from setups import *
from movement import *
from mazes import farm_treasure
from sunflowers import farm_sunflower

do_a_flip()

farm_sunflower()
cycle(deplow)
farm_treasure(2000)

pet_the_piggy()
```
### Unlocking `Simulate`
__main__
``` python
...
do_a_flip()

farm_sunflower()
cycle(deplow)
farm_treasure(5000)

pet_the_piggy()
```
### Unlocking `Megafarm (II)`
__main__
``` python
...
do_a_flip()

farm_treasure(8000)

pet_the_piggy()
```