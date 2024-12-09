import random
fix=random.randint(1,10)
i=1
while i<=3:
    n=int(input("Guess number"))
    if fix==n:
        print("You won the Game")
        break
    else:
        print("Your guess is wrong")
    i+=1
else:
    print("You lost the game")
print("Game Over")
    
