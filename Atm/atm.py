def checkbalance(amount):
    return amount
def Deposit(amount,m):
    return amount+m
def withdraw(amount,n):
    return amount-n
    


amount=10000
s=1
while s==1:
    print("1.Check Balance\n2.Deposit\n3.Withdraw\n")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        bal=checkbalance(amount)
        print("\nAvailable Balance:",bal)
    elif choice==2:
        m=int(input("Enter amount to Deposit:"))
        amount=Deposit(amount,m)
        print("Successfully Deposited")
    elif choice==3:
        n=int(input("Enter amount to Withdraw:"))
        if n>amount:
            print("Insufficient Balance")
        else:
            amount=withdraw(amount,n)
            print("Successfully completed")
    else:
        print("Choose valid option")
    s=int(input("\nContinue/Exit?\nEnter 1 to Continue 0 to Exit"))
    print("\n")
print("-----THANK YOU!!!-----")
