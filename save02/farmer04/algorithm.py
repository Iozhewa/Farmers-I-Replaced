from movement import goto, rotation
from setups import *
from poly import poly_farm
from sunflowers import farm_sunflower
from pumpkins import farm_pumpkin

do_a_flip()
change_hat(Hats.Rice_Hat)

goto(0, 0)
cycle(collect)
while num_items(Items.Pumpkin) < 6.4*10**4:
	if num_items(Items.Power) < 200:
		farm_sunflower()
	if num_items(Items.Carrot) < 5*10**3:
		poly_farm(Entities.Carrot, 2*10**4)
	farm_pumpkin(num_items(Items.Pumpkin)+100)

pet_the_piggy()