import time
print("Please insert your ATM CARD")
time.sleep(5)
password = 1234
pin = int(input("Enter your ATM PIN"))
balance = 5000


if pin == password:
    while True:

        print("""
        1 == balance
        2 == withdraw balance 
        3 == deposit balance
        4 == exit
        """
        )
        try : 
            option=int(input("Please enter your choice "))
        except :
            print("Please enter valid option")

        if option == 1:
            print(f"Your current balance is {balance}")
            print("------------------------------------")
            print("------------------------------------")
            print("------------------------------------")


        if option == 2:
            withdraw_amount=int(input("Please enter withdraw_amount "))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your updated balance is {balance}")
            print("------------------------------------")
            print("------------------------------------")
            print("------------------------------------")
        
        if option == 3:
            deposit_amount=int(input("Please enter deposit_amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your amount")
            print(f"your updated balance is {balance}")
            print("------------------------------------")
            print("------------------------------------")
            print("------------------------------------")
        
        if option == 4:
            break
else:
    print("Wrong PIN!! Please try again.")

