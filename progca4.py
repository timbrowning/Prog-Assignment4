import sys
import pandas as pd

def menu(data):
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
    1: Enter utility bill details: utility company, name of the customer, date of the bill, the amount, and a flag indicating whether the bill is debit or credit
    2: writing and reading these utility bills to a text file
    3: Provide a report that lists years, total credited and total debited
    4: Provide a report that shows the most popular utility company
    5: Quit/Log Out

    Please enter your choice: """)

    if choice == "1":
        enterdetails(data)
    elif choice == "2" or choice =="b":
        return()
    elif choice == "3" or choice =="c":
        return()
    elif choice=="4" or choice=="d":
        return()
    elif choice=="5" or choice=="q":
        sys.exit
    else:
        print("You must only select either 1,2,3,4.")
        print("Please try again")
        menu()

def enterdetails(data):
    utilityCompany = input("Enter Utility Company?\n>")
    menu(data)
    

data = pd.read_csv("results.csv")
data
menu(data)