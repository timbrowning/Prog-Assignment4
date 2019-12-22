import sys
import pandas as pd
import datetime

from Write_text import WriteToText
from report3 import Report3
from report4 import Report4
from report5 import Report5
from report6 import Report6
from report7 import Report7

class Menu:

    def display_menu(self, data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                     credit_or_debit):
        print("\n                                                            ************MAIN MENU**************")
        print()
        choice = input("""
        1: Enter utility bill details: utility company, name of the customer, date of the bill, the amount, and a flag indicating whether the bill is debit or credit
        2: Write file to txt file
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
            company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount, credit_or_debit = self.enter_details()
            print("                   Customer Details")
            print("*********************************************************")
            print("Company Name: ", company_name)
            print("Customer Name: ", customer_name)
            print("Date: ", year_of_bill, "/", month_of_bill, "/", day_of_bill, sep="")
            print("Amount: $", amount, sep="")
            print("Credit or Debit: \"", credit_or_debit, '"', sep="")
            print("*********************************************************\n")
            print("Your Entry has been printed above\n")
            input("Press Enter to continue...\n")
            self.display_menu(data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)
        elif choice == "2":
            WriteToText.to_text(data_c, data, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill,
                                amount, credit_or_debit)
            self.display_menu(data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)
            return ()
        elif choice == "3":
            Report3.report3(data_c, data)
            self.display_menu(data_c,company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)
            return ()
        elif choice == "4":
            Report4.report4(data_c, data)
            self.display_menu(data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)
            return ()
        elif choice == "5":
            Report5.report5(data_c, data)
            self.display_menu(data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)
            return ()
        elif choice == "6":
            Report6.report6(data_c, data)
            self.display_menu(data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)
            return ()
        elif choice == "7":
            Report7.report7(data_c, data)
            self.display_menu(data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)
            return ()
        elif choice == "8":
            return ()
        elif choice == "8":
            return ()
        elif choice == "0":
            sys.exit()
        else:
            print("\nYou must only select either 1,2,3,4,5,6,7,8,9,0")
            input("Press Enter to continue...\n")
            self.display_menu(data_c, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                              credit_or_debit)

    def enter_details(self):
        company_name = self.enter_company_name()
        customer_name = self.enter_customer_name(company_name)
        year_of_bill = self.enter_year(company_name, customer_name)
        month_of_bill = self.enter_month(company_name, customer_name, year_of_bill)
        day_of_bill = self.enter_day(company_name, customer_name, year_of_bill, month_of_bill)
        amount = self.enter_amount(company_name, customer_name, year_of_bill, month_of_bill, day_of_bill)
        credit_or_debit = self.enter_credit_or_debit(company_name, customer_name, year_of_bill, month_of_bill,
                                                     day_of_bill, amount)

        return company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount, credit_or_debit

    def enter_company_name(self):
        temp = ""
        while temp != 'y':
            company_name = input("Enter Utility Company?\n>")
            print("Is \"", company_name, "\" correct? (Enter \"y\" for yes or enter \"n\" for no )", sep="")
            temp = input(">")
            if temp == "Y" or temp == "y":
                print("The Company Name \"", company_name, "\" has been recorded", sep="")
                input("Press Enter to continue...\n")
                return company_name

    def enter_customer_name(self, company_name):
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

    def enter_year(self, company_name, customer_name):
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

    def enter_month(self, company_name, customer_name, year_of_bill):
        temp = ""
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
            month = 0
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

    def enter_day(self, company_name, customer_name, year_of_bill, month_of_bill):
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

    def enter_amount(self, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill):
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

    def enter_credit_or_debit(self, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount):
        temp = ""
        while temp != 'y':
            credit_debit = ''
            print("*********************************************************")
            print("Company Name: ", company_name)
            print("Customer Name: ", customer_name)
            print("Year:", year_of_bill, " Month:", month_of_bill, " Day: ", day_of_bill, sep="")
            print("Amount: $", amount, sep="")
            print("*********************************************************\n")
            while credit_debit != 'c' and credit_debit != 'd':
                credit_debit = input("Please enter \"c\" for Credit and \"d\" for Debit? \n>")
                if credit_debit != 'c' and credit_debit != 'd':
                    print("Invalid Input")
                    input("Press Enter to try again...\n")
            if credit_debit == 'c' or credit_debit == "C":
                credit_debit = "Credit"
            if credit_debit == "d" or credit_debit == "D":
                credit_debit = "Debit"
            print("Is \"", credit_debit, "\" correct? (Enter \"y\" for yes or enter \"n\" for no)", sep="")
            temp = input(">")
            if temp == "Y" or temp == "y":
                print("The bill is: \"", credit_debit, "\"", " and has been recorded", sep="")
                input("Press Enter to continue...\n")
                return credit_debit


if __name__ == "__main__":
    data = pd.read_csv("results.csv",
                       names=['company_name', 'customer_name', 'year_of_bill', 'month_of_bill', 'day_of_bill',
                              'amount', 'credit_or_debit'])
    company_name = ''
    customer_name = ''
    year_of_bill = 0
    month_of_bill = 0
    day_of_bill = 0
    amount = 0
    credit_or_debit = ''
    Menu().display_menu(data, company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount,
                        credit_or_debit)
