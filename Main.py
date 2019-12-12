import sys
import pandas as pd
import datetime


def menu():
    choice = 10
    print("\n                                                            ************MAIN MENU**************")
    print()
    choice = input("""
1: Enter utility bill details: utility company, name of the customer, date of the bill, the amount, and a flag indicating whether the bill is debit or credit
2: Writing and reading these utility bills to a text file
3: Provide a report that lists years, total credited and total debited
4: Provide a report that shows the most popular utility company.  The most popular utility company is the one with the most bills against that provider
5: Provide a report that shows the bills in date order.
6: Provide another report that displays the highest amount for a bill that is a credit, and one for a debit.
7: Provide a report to indicate how successful the company is.  This should display the total number of bills.
8: Provide a report to calculate the average spent per period of time (month/year) that can be entered by the user.
9: Provide a report to calculate the average time between bills.
0: Quit

Please enter your choice number 1-9 : """)

    if choice == "1":
        enter_details()
        menu()
    elif choice == "2":
        return ()
    elif choice == "3":
        return ()
    elif choice == "4":
        return ()
    elif choice == "5":
        return ()
    elif choice == "6":
        return ()
    elif choice == "7":
        return ()
    elif choice == "8":
        return ()
    elif choice == "8":
        return ()
    elif choice == "0":
        sys.exit
    else:
        print("\nYou must only select either 1,2,3,4,5,6,7,8,9,0")
        input("Press Enter to continue...\n")
        menu(data)


def enter_details():
    company_name = enter_company_name()
    customer_name = enter_customer_name(company_name)
    year_of_bill = enter_year(company_name, customer_name)
    month_of_bill = enter_month(company_name, customer_name, year_of_bill)
    day_of_bill = enter_day(company_name, customer_name, year_of_bill, month_of_bill)
    amount = enter_amount(company_name, customer_name, year_of_bill, month_of_bill, day_of_bill)


def enter_company_name():
    temp = ""
    while temp != 'y':
        company_name = input("Enter Utility Company?\n>")
        print("Is \"", company_name, "\" correct? (Enter \"y\" for yes or enter \"n\" for no )", sep="")
        temp = input(">")
        if temp == "Y" or temp == "y":
            print("The Company Name \"", company_name, "\" has been recorded", sep="")
            input("Press Enter to continue...\n")
            return company_name


def enter_customer_name(company_name):
    temp = ""
    while temp != 'y':
        print("*********************************************************")
        print("Company Name: ", company_name)
        print("*********************************************************\n")
        name = input("Enter Customer Name?\n>")
        print("Is \"", name, "\" correct? (Enter \"y\" for yes or enter \"n\" for no)", sep="")
        temp = input(">")
        if temp == "Y" or temp == "y":
            print("The Customer Name \"", name, "\" has been recorded", sep="")
            input("Press Enter to continue...\n")
            return name


def enter_year(company_name, customer_name):
    temp = ""
    while temp != 'y':
        year = 0
        print("*********************************************************")
        print("Company Name: ", company_name)
        print("Customer Name: ", customer_name)
        print("*********************************************************\n")
        while year < 1000 or year > 9999:
            try:
                year = int(input("Enter Date: Starting with Year in format  \"YYYY\" e.g \"2017\"  ?\n>"))
                if year < 1000 or year > 9999:
                    print("Invalid Input")
                    input("Press Enter to try again...\n")
            except:
                print("Invalid Input")
                input("Press Enter to try again...\n")
        print("Is \"", year, "\" correct? (Enter \"y\" for yes or enter \"n\" for no)", sep="")
        temp = input(">")
        if temp == "Y" or temp == "y":
            print("The Year: \"", year, "\" has been recorded", sep="")
            input("Press Enter to continue...\n")
            return year


def enter_month(company_name, customer_name, year_of_bill):
    temp = ""
    month = 0
    monthdict = {1: 'Janauary',
                 2: 'February',
                 3: 'March',
                 4: 'April',
                 5: 'May',
                 6: 'June',
                 7: 'July',
                 8: 'August',
                 9: 'September',
                 10: 'October',
                 11: 'November',
                 12: 'December'
                 }
    while temp != 'y':
        print("*********************************************************")
        print("Company Name: ", company_name)
        print("Customer Name: ", customer_name)
        print("Year: ", year_of_bill)
        print("*********************************************************\n")
        while month < 1 or month > 12:
            try:
                month = int(input("Enter Month  \"MM\" e.g \"6 = June\"  ?\n>"))
                if month < 1 or month > 12:
                    print("Invalid Input")
                    input("Press Enter to try again...\n")
            except:
                print("Invalid Input")
                input("Press Enter to try again...\n")
        print("Is \"", month, "\" correct? (Enter \"y\" for yes or enter \"n\" for no)", sep="")
        temp = input(">")
        if temp == "Y" or temp == "y":
            print("The Month: \"", month, "\"", " - ", monthdict[month], " has been recorded", sep="")
            input("Press Enter to continue...\n")
            return month


def enter_day(company_name, customer_name, year_of_bill, month_of_bill):
    temp = ""
    while temp != 'y':
        day = 0
        print("*********************************************************")
        print("Company Name: ", company_name)
        print("Customer Name: ", customer_name)
        print("Year: ", year_of_bill)
        print("Month: ", month_of_bill)
        print("*********************************************************\n")
        while day < 1 or day > 31:
            try:
                day = int(input("Enter Day  \"DD\" e.g \"24\"  ?\n>"))
                if day < 1 or day > 31:
                    print("Invalid Input")
                    input("Press Enter to try again...\n")
            except:
                print("Invalid Input")
                input("Press Enter to try again...\n")
        print("Is \"", day, "\" correct? (Enter \"y\" for yes or enter \"n\" for no)", sep="")
        temp = input(">")
        if temp == "Y" or temp == "y":
            print("The Day: \"", day, "\"", " has been recorded", sep="")
            input("Press Enter to continue...\n")
            return day


def enter_amount(company_name, customer_name, year_of_bill, month_of_bill, day_of_bill):
    temp = ""
    while temp != 'y':
        amount = 1
        print("*********************************************************")
        print("Company Name: ", company_name)
        print("Customer Name: ", customer_name)
        print("Year:", year_of_bill, " Month:", month_of_bill, " Day: ", day_of_bill, sep="")
        print("*********************************************************\n")
        try:
            amount = float(input("Enter amount? \n>"))
        except:
            print("Invalid Input")
            input("Press Enter to try again...\n")
        print("Is \"", amount, "\" correct? (Enter \"y\" for yes or enter \"n\" for no)", sep="")
        temp = input(">")
        if temp == "Y" or temp == "y":
            print("The Amount: \"", amount, "\"", " has been recorded", sep="")
            input("Press Enter to continue...\n")
            return amount


if __name__ == "__main__":
    data = pd.read_csv("results.csv")
    menu()
