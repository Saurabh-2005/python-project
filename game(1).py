a=input("enter a your name :")
print("Welcome Mr.",a,"your game is Start")
import random
Target=random.randint(1,100) 
while True:
    userChoice=(input("Guess the number or Quit(Q):"))
    if(userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if(userChoice==Target):
        print("Your are winner")
        break
    elif(userChoice<Target):
        print("your number is small,Guess again.")
    else:
        print("your number is big,Guess again.")
print("---------------------Game over---------------------")