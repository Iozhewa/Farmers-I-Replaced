# Farmers I Replaced
Imagine liking a game so much you blog about it...


__Table of Contents__
1. [Bulding Blocks (Singular Code)](#building-blocks)
2. [Delegations (First Modules)](#delegations)
3. [Sunflowers and Pumpkins (working title](#sunflowers-and-pumpkins)

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