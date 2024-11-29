from time import sleep

user_name="abdo"
password=707
Account_amount=20000
counter=3

while True:
    UserName_enterd=input("Enter your User Name ")
    password_enterd=int(input("Enter a password "))

    if password==password_enterd and user_name==UserName_enterd:
        print(f"welcome {user_name}")
        withdrawal=int(input("Enter the withdrawal amount "))
        if withdrawal <= Account_amount:
            print("prossing...")
            sleep(3)
            print(f"{withdrawal} has been deducted from your bank account")
            Account_amount-=withdrawal
            print(f"Your account amount has become {Account_amount}")
            break
        else:
            print("inviled amount")
    else:
        print("the UserName or password don't correct")
        print("please try again ")
        if counter==3:
            counter+=1
            print("you reach your limit")
            print("Please check your bank account!!!")
            break
