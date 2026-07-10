print("==========ATM MACHINE===========")
print("ENTER THE SERIAL NO. OF THE FOLLOWING SERVICES TO WORK")

print("""         1. CHECK BALANCE
         2. DEPOSIT MONEY
         3. WITHDRAW MONEY
         4. EXIT""")

bal = 1000

num = int(input(""))

if num < 0 or num > 4:
    print("WRONG INFO, PLEASE TRY AGAIN")

elif num == 1:
    print(f"YOUR ACCOUNT BALANCE IS Rs.{bal}")

elif num == 2:
    print("ENTER THE AMOUNT YOU ARE DEPOSITING")
    dep = int(input(""))
    add = bal + dep
    print(f"NOW YOUR TOTAL BALANCE IS Rs.{add}")

elif num == 3:
    print("ENTER THE AMOUNT OF MONEY YOU ARE GOING TO WITHDRAW")
    wit = int(input(""))

    if wit <= bal:
        sub = bal - wit
        print(f"NOW YOUR BALANCE IS Rs.{sub}")
    else:
        print("INSUFFICIENT BALANCE")

elif num == 4:
    print("THANK YOU FOR CHOOSING OUR BANK. THE PROCESS IS DONE.")

print("============================================================")
# END OF CODE