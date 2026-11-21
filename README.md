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
### Unlocking `mining (III)`, `coal (II)`, `rice (II)`, `bamboo (I)`, `bamboo (II)`, `petrified pumpkins (I)`, 
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
### Unlocking `mining (IV)`, `coal (III)`, `rice (III)`
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