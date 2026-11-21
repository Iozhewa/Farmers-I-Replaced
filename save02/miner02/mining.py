from movement import *
from setups import *

def coal():
	if get_ground_type() == Grounds.Coal:
		dig()

def iron():
	if get_ground_type() == Grounds.Iron:
		dig()

def evens(sequence=range(5)):
	result = []
	for elem in sequence:
		if elem % 2 == 0:
			result.append(elem)
	return result

def dig_block():
	delta_coal = num_items(Items.Coal)
	while delta_coal > 0:
		for x in evens(range(get_world_size())):
			for y in (6, 9):
				goto(x, y)
				for _ in range(0, 4):
					dig()
		delta_coal -= num_items(Items.Coal)

def dig_coal():
	found_clay = False
	while not(found_clay):
		for x in evens(range(get_world_size())):
			for y in (6, 9):
				goto(x, y)
				for _ in range(0, 3):
					dig()
					found_clay = found_clay or get_ground_type() == Grounds.Clay
		cycle(coal)

def farm_rice():
	found_rock = False
	while not(found_rock):
		goto(get_world_size()-1, get_world_size()-1)
		found_rock = get_ground_type() == Grounds.Rock
		#cycle(terrace)

def dig_iron(withSearch=True):
	if withSearch:
		cycle(collect)
	counter = 0
	while counter < 10:
		prospect = prospect_iron()
		while prospect != None:
			move(prospect)
			prospect = prospect_iron()
		gains = num_items(Items.Iron)
		while gains > num_items(Items.Iron):
			for _ in range(5):
				dig()
		cycle(iron)
		counter += 1