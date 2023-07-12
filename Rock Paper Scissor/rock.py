import random
l=["Rock","Paper","Scissors"]
play=1

while play==1:
    computer=random.choice(l).lower()
    user=input("Enter your choice(Rock,Paper,Scissors):").lower()
    print("\nYour Choice:",user)
    print("Computer's Choice:",computer,"\n")
    if user==computer:
        print("Both Won!")
    elif user=="rock":
        if computer=="paper":
            print("Computer Wins!")
        elif computer=="scissors":
            print("You Win!")
    elif user=="paper":
        if computer=="rock":
            print("You Win!")
        elif computer=="scissors":
            print("Computer Wins!")
    elif user=="scissors":
        if computer=="rock":
            print("Computer Wins!")
        elif computer=="paper":
            print("You Win!")
    play=int(input("\nWant to play Again? \nEnter 1 to play , 0 to Exit"))
   
