import sys
import pandas as pd
import datetime


class WriteToText:
    def to_text(self):
        pd.set_option('display.max_columns', 10)
        data = pd.read_csv("results.csv", names=['company_name', 'customer_name', 'year_of_bill', 'month_of_bill', 'day_of_bill',' amount', 'credit_or_debit'])
        new_row = pd.Series(["Google", "Tim", 2019, 12, 13, 124124.0, "Credit"], index=["company_name", 'customer_name', 'year_of_bill', 'month_of_bill', 'day_of_bill', ' amount', 'credit_or_debit'])
        print(type(new_row))
        data = data.append(new_row, ignore_index=True)

        data.to_csv(r'Q2.csv')
        print("The dataset \"results.csv\" has been added to a text file called \"Q2.txt\" ^")
        input("Press Enter to continue...\n")
        return


if __name__ == '__main__':
    WriteToText().to_text()
