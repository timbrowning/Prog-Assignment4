import sys
import pandas as pd
import datetime


class WriteToText:
    def to_text(self, data,  company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount, credit_or_debit):
        if year_of_bill != 0:
            new_row = pd.Series([company_name, customer_name, year_of_bill, month_of_bill, day_of_bill, amount, credit_or_debit],
                            index=["company_name", 'customer_name', 'year_of_bill', 'month_of_bill', 'day_of_bill',
                                   ' amount', 'credit_or_debit'])
            data = data.append(new_row, ignore_index=True)
            data.to_csv(r'Q2.txt')
            print("The dataset \"results.csv\" and the entry from Q1 has been added to a text file called \"Q2.txt\" ^")
            input("Press Enter to continue...\n")
        else:
            print("Please Enter bill details from question 1")
            input("Press Enter to continue...\n")
            return data


if __name__ == '__main__':
    WriteToText()
