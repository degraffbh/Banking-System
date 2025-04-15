import mysql.connector
import time

connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'Brook9!!!')
cursor = connection.cursor()
testQuery = ('SELECT * FROM user')
cursor.execute(testQuery)
for item in cursor:
    print(item)
cursor.close()

def login_screen():
    print("\nBen's Banking System\nLogin Page\n")

    login_or_new = input("Sign in (s) or make a new account (n)? ")
    if (login_or_new == "s"):
        account_number = input("Please enter your account number: ")
        pin = int(input("Please enter your pin: "))

        #Add code to check if account number is in database and if pin matches
    else:
        name = input("What is your name? ")
        account_number = input("Please enter an account number: ")
        valid_pin = False
        while (valid_pin == False):
            pin = int(input("Please enter a 4 digit pin: "))
            if (len(str(pin)) == 4):
                valid_pin = True
        balance = input("How much money would you like to deposit as your starting balance? ")

        sql = "INSERT INTO user (account_num, pin, balance, account_name) VALUES (%s, %s, %s, %s)"
        val = (account_number, pin, balance, name)
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()

        print(f"Ben's Banking account {account_number} created sucessfully!")

def menu_page():
    isUsingApp = True
    while isUsingApp == True:
        print("\nWhat would you like to do today?")
        print("(1) Check Balance")
        print("(2) Deposit")
        print("(3) Withdraw")
        print("(4) Create Account")
        print("(5) Delete Account")
        print("(6) Modify Account")
        print("(7) Exit")
        answer = int(input("> "))

        #Need to code all the actions 
        match answer:
            case 1:
                getBalanceQuery = ('SELECT balance FROM user WHERE account_name = "Ben DeGraff"') #Need to add account_name varaible
                cursor = connection.cursor()
                cursor.execute(getBalanceQuery)
                for item in cursor:
                    print(f'\nYour current balance is ${str(item)[1:len(item)-3]}')
                cursor.close()
                time.sleep(1.5)
            case 2:
                new_balance = int(input("How much money would you like to deposit? "))
                getBalanceQuery = ('SELECT balance FROM user WHERE account_name = "Ben DeGraff"') #Need to add account_name varaible
                cursor = connection.cursor()
                cursor.execute(getBalanceQuery)
                for item in cursor:
                    new_balance += int(str(item)[1:len(item)-3])
                cursor.close()

                updateBalanceQuery = ('UPDATE user SET balance = %s WHERE account_name = %s') 
                val = (new_balance, "Ben DeGraff")
                cursor = connection.cursor()
                cursor.execute(updateBalanceQuery, val)
                connection.commit()
                cursor.close()
                print("Balance Updated")
            case 3:
                new_balance = int(input("How much money would you like to withdraw? "))
                getBalanceQuery = ('SELECT balance FROM user WHERE account_name = "Ben DeGraff"') #Need to add account_name varaible
                cursor = connection.cursor()
                cursor.execute(getBalanceQuery)
                for item in cursor:
                    new_balance = int(str(item)[1:len(item)-3]) - new_balance
                cursor.close()

                updateBalanceQuery = ('UPDATE user SET balance = %s WHERE account_name = %s') 
                val = (new_balance, "Ben DeGraff")
                cursor = connection.cursor()
                cursor.execute(updateBalanceQuery, val)
                connection.commit()
                cursor.close()
                print("Balance Updated")
            case 4:
                print("\nCreate Account")
            case 5:
                print("\nDelete Account")
            case 6:
                print("\nModify Account")
            case 7:
                print("\nHave a good rest of your day!")
                isUsingApp = False
            case _:
                print("\nInvalid command")

login_screen()
menu_page()

connection.close()