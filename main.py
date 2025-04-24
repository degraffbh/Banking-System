import mysql.connector
import time

connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'Brook9!!!')
cursor = connection.cursor()
testQuery = ('SELECT * FROM user')
cursor.execute(testQuery)
for item in cursor:
    print(item)
cursor.close()

USER_ACCOUNT_NAME = None

def login_screen():
    print("\nBen's Banking System\nLogin Page\n")

    login_or_new = input("Sign in (s) or make a new account (n)? ")
    if (login_or_new == "s"):
        isValid = False
       
        while isValid == False:
            validNum = False
            validPin = False
            account_number = int(input("Please enter your account number: "))
            pin = int(input("Please enter your pin: "))

            #Checking for valid account_num
            checkAccountQuery = ('SELECT %s FROM user WHERE account_num = %s') 
            val = (pin, account_number)
            cursor = connection.cursor()
            cursor.execute(checkAccountQuery, val)
            for item in cursor:
                validNum = True
            cursor.close()

            #Checking for valid pin
            checkPinQuery = ('SELECT %s FROM user WHERE pin = %s') 
            val = (account_number, pin)
            cursorTwo = connection.cursor()
            cursorTwo.execute(checkPinQuery, val)
            for item in cursorTwo:
                validPin = True
            cursorTwo.close()

            if validNum == True and validPin == True:
                isValid = True
                getNameQuery = ('SELECT account_name FROM user WHERE account_num = %s')
                val = (account_number,)
                cursorThree = connection.cursor()
                cursorThree.execute(getNameQuery, val)
                for item in cursorThree:
                    USER_ACCOUNT_NAME = str(item)[2:len(item)-4]
                    print(f'\nWelcome {str(item)[2:len(item)-4]}!')
                cursorThree.close()
            else:
                print("Login information incorrect. Please try again.")
            
            
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

        USER_ACCOUNT_NAME = name
        print(f"Ben's Banking account {account_number} created sucessfully!")

def menu_page():
    isUsingApp = True
    while isUsingApp == True:
        print("\nWhat would you like to do today?")
        print("(1) Check Balance")
        print("(2) Deposit")
        print("(3) Withdraw")
        print("(4) Delete Account")
        print("(5) Modify Account")
        print("(6) Exit")
        answer = int(input("> "))

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
                isValid = False
                while isValid == False:
                    new_balance = int(input("How much money would you like to withdraw? "))
                    getBalanceQuery = ('SELECT balance FROM user WHERE account_name = "Ben DeGraff"') #Need to add account_name varaible
                    cursor = connection.cursor()
                    cursor.execute(getBalanceQuery)
                    for item in cursor:
                        if int(str(item)[1:len(item)-3]) >= new_balance:
                            new_balance = int(str(item)[1:len(item)-3]) - new_balance
                            isValid = True
                        else:
                            print("You don't have that much money in your account. Please try again.")
                    cursor.close()
               
                updateBalanceQuery = ('UPDATE user SET balance = %s WHERE account_name = %s') 
                val = (new_balance, "Ben DeGraff")
                cursor = connection.cursor()
                cursor.execute(updateBalanceQuery, val)
                connection.commit()
                cursor.close()
                print("Balance Updated")
            case 4:
                print("\nDelete Account")
            case 5:
                print("\nModify Account")
            case 6:
                print("\nHave a good rest of your day!")
                isUsingApp = False
            case _:
                print("\nInvalid command")

login_screen()
menu_page()

connection.close()