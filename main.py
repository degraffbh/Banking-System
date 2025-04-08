import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'pokemon', password = 'Brook9!!!')
cursor = connection.cursor()
testQuery = ('SELECT * FROM pokemon_type')
cursor.execute(testQuery)
for item in cursor:
    print(item)

cursor.close()
connection.close()

def login_screen():
    print("\nBen's Banking System\nLogin Page\n")

    login_or_new = input("Sign in (s) or make a new account (n)? ")
    if (login_or_new == "s"):
        account_number = input("Please enter your account number: ")
        pin = int(input("Please enter your pin: "))

        #Add code to check if account number is in database and if pin matches
    else:
        account_number = input("Please enter an account number: ")
        valid_pin = False
        while (valid_pin == False):
            pin = int(input("Please enter a minimum 8 digit pin: "))
            if (len(str(pin)) >= 8):
                valid_pin = True

        #Add code to add account to database

        print(f"Ben's Banking account {account_number} created sucessfully!")

def menu_page():
    print("\nWhat would you like to do today?")
    print("(1) Check Balance")
    print("(2) Deposit")
    print("(3) Withdraw")
    print("(4) Create Account")
    print("(5) Delete Account")
    print("(6) Modify Account")
    answer = int(input("> "))

    #Need to code all the actions 
    match answer:
        case 1:
            print("\nCheck Balance")
        case 2:
            print("\nDeposit")
        case 3:
            print("\nWithdraw")
        case 4:
            print("\nCreate Account")
        case 5:
            print("\nDelete Account")
        case 6:
            print("\nModify Account")
        case _:
            print("\nInvalid command")

login_screen()
menu_page()