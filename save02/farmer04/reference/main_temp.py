from movement import goto
from hay import farm_hay
from bushes import farm_bush
from carrots import farm_carrot
from trees import farm_tree
from sunflowers import farm_sunflower
from pumpkins import farm_pumpkin

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