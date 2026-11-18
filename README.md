# Farmers-I-Replaced
Imagine liking a game so much you blog about it...


__Table of Contents__
1. [Bulding Blocks (Singular Code)](#building-blocks)
2. [Delegations (First Modules)](#delegations)

## Building Blocks
__Hat__: Straw
### Unlocking `while`
``` python
do_a_flip()
harvest()
harvest()
harvest()
harvest()
harvest()  # just getting 5 wheat
```
### Unlocking `speed (I)`
``` python
do_a_flip()
while True: # No conditions unlocked yet...
    harvest()
pet_the_piggy() 
```
### Unlocking `expand (I)`
``` python
do_a_flip()
while True:
	if can_harvest():
		harvest()
pet_the_piggy()
```
### Unlocking `plant`
``` python
do_a_flip()
while True:
	move(North)
	if can_harvest():
		harvest()
pet_the_piggy()
```

__Hat__: Brown
### Unlocking `speed (II)` and `expand (II)`
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
## Delegations