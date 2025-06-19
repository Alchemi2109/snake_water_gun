
import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
usstr = input("Enter you choice: ")
usdict = {"s" : 1, "w" : -1, "g" :0 }
resversdict = {1 : "snake", -1: "water", 0 : "gun"}
us = usdict[usstr]

print(f"you chose {resversdict[us]}\ncomputer chose {resversdict[computer]}")

if(computer == us):
    print("It's a draw")

else:
    if(computer == -1 and us == 1):
        print("You win!")

    elif(computer == -1 and us == 0):
        print("You lose!")

    elif(computer == 1 and us == 0):
        print("You win!")

    elif(computer == 1 and us == -1):
        print("You lose!")

    elif(computer == 0 and us == 1):
        print("You lose!")

    elif(computer == 0 and us == -1):
        print("You win!")

    else:
        print("something went wrong")