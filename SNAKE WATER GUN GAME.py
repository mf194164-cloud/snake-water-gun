'''Rules and Interactions
Snake vs. Water: Snake drinks water, so the snake wins.
Water vs. Gun: Water drowns the gun, so water wins.
Gun vs. Snake: Gun kills the snake, so the gun wins.
Same Choice: If both players choose the same option, the result is a draw.'''

'''snake = 1
water = 2
gun = 3'''

import random
random_computer = random.randint(1,3) # int computer 

dict_name= {1:"snake",2:"water",3:"gun"}
dict_name_rev= {"snake":1,"water":2,"gun":3}
computer = dict_name[random_computer] #str computer


you_str = input("enter snake or gun or water: ") #str you
you = dict_name_rev[you_str] #int you

print(f"YOU CHOOSE >>>>>>>>>> {you_str}")
print(f"COMPUTER CHOOSE>>>>>> {computer}")

if random_computer == you:
    print("MATCH IS DRAW")
else:
    if random_computer==1 and you==2:
        print("COMPUTER WON !!!!!!!")
    elif random_computer==1 and you==3:
        print("YOU WON !!!!!!!")
    elif random_computer==2 and you==1:
        print("YOU WON !!!!!!!")
    elif random_computer==2 and you==3:
        print("COMPUTER WON !!!!!!!")
    elif random_computer==3 and you==1:
        print("COMPUTER WON !!!!!!!")
    elif random_computer==3 and you==2:
        print("YOU WON !!!!!!!")


   


