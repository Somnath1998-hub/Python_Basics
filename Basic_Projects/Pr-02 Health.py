health = 50

difficulty_level =2

import random

portion_health = random.randint (25 , 100)

health = int(health + portion_health / difficulty_level)

print (health)

