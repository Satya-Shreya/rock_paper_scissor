import random
while True:
    choices=["paper","rock","scissors"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock,papaer,scissors?").lower()
    if player==computer:
        print("computer:",computer)
        print("player:",player)
        print("tie")
    elif player=="rock":
        if computer=="paper":
            print("computer:",computer)
            print("player:",player)
            print("you lose")
        if computer=="scissors":
            print("computer:",computer)
            print("player:",player)
            print("you won")
    elif player=="paper":
        if computer=="rock":
            print("computer:",computer)
            print("player:",player)
            print("you won")
        if computer=="scissors":
            print("computer:",computer)
            print("player:",player)
            print("you loose")
    elif player=="scissors":
        if computer=="paper":
            print("computer:",computer)
            print("player:",player)
            print("you won")
        if computer=="rock":
            print("computer:",computer)
            print("player:",player)
            print("you losse")
    play=input("play again?(yes/no)").lower()
    if play!="yes":
        break
print("bye")
