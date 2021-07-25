""" Health Potion project :-

Here by using variable, number and the random module I have created a functionality required for the health potion
to work.
Initially the character has some Health amount and the game has three difficulty level 
Easy: 1
Medium: 2
Hard: 3
Depending on the what difficulty is selected the amount of health the person get from the potion is decided.
For higher difficulty the amount of health the person get is less and vice versa.   
"""


health = 50                                         #Initial Health

difficulty_level = 2                                 #Difficulty_level :Medium

import random

portion_health = random.randint (25 , 100)

health = int(health + portion_health / difficulty_level)

print (health)

