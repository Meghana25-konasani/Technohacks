import random
import numpy as np
def check(a,s):
    if a[0][0]=="X" and a[1][1]=="X" and a[2][2]=="X":
        s=s+1
    elif a[0][2]=="X" and a[1][1]=="X" and a[2][0]=="X":
        s=s+1
    elif a[0][0]=="O" and a[1][1]=="O" and a[2][2]=="O":
        s=s+2
    elif a[0][2]=="O" and a[1][1]=="O" and a[2][0]=="O":
        s=s+2
    else:
        for i in range(0,3):
            if a[i][0]=="X" and a[i][1]=="X" and a[i][2]=="X":
                s=s+1
                break
            elif a[i][0]=="O" and a[i][1]=="O" and a[i][2]=="O":
                s=s+2
                break
            elif a[0][i]=="X" and a[1][i]=="X" and a[2][i]=="X":
                s=s+1
                break
            elif a[0][i]=="O" and a[1][i]=="O" and a[2][i]=="O":
                s=s+2
                break
    
    return s


m=[0,1,2]
play=1
while play==1:
    a=np.array([["_","_","_"],["_","_","_"],["_","_","_"]])
    s=0
    choice=int(input("Mode of Play?\n1.2 Players\n2.Vs Computer"))
    for i in range(0,3):
        for j in range(0,3):
            print(a[i][j],end=" ")
        print(end="\n")
    while s==0:
        print("\n---PLAYER1---\n")
        player1_1=int(input("Enter i:"))
        player1_2=int(input("Enter j:"))
        while a[player1_1][player1_2]=="X" or a[player1_1][player1_2]=="O":
            print("Block is not EMPTY! Enter Again")
            player1_1=int(input("Enter i:"))
            player1_2=int(input("Enter j:"))
        a[player1_1][player1_2]="X"
        for i in range(0,3):
            for j in range(0,3):
                print(a[i][j],end=" ")
            print(end="\n")
        if np.any(a=="_"):
            if choice==1:
                print("\n---PLAYER2---\n")
                player2_1=int(input("Enter i:"))
                player2_2=int(input("Enter j:"))
                while (player1_1==player2_1 and player1_2==player2_2) or (a[player2_1][player2_2]=="X" or a[player2_1][player2_2]=="O"):
                    print("Block is not EMPTY! Enter Again")
                    player2_1=int(input("Enter i:"))
                    player2_2=int(input("Enter j:"))
                a[player2_1][player2_2]="O"
            elif choice==2:
                computer1=random.choice(m)
                computer2=random.choice(m)
                while (player1_1==computer1 and player1_2==computer2) or (a[computer1][computer2]=="X" or a[computer1][computer2]=="O"):
                    computer1=random.choice(m)
                    computer2=random.choice(m)
                a[computer1][computer2]="O"
            for i in range(0,3):
                for j in range(0,3):
                    print(a[i][j],end=" ")
                print(end="\n")
        else:
            m=0    

        s=check(a,s)
    if s==1:
        print("You Win!")
    elif s==2:
        if choice==1:
            print("Player2 Wins!")
        else:
            print("Computer wins!")
    elif m==0:
        print("No one Won!")
    play=int(input("\nWant to play Again? \nEnter 1 to play , 0 to Exit"))

