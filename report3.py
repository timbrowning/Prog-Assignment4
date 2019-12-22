import sys
import pandas as pd
import datetime


class Report3:
    def report3(self, data):

        group2 = data.groupby(['year_of_bill', 'credit_or_debit'])['amount'].agg('sum')

        print(group2)
        input("Press Enter to display menu...\n")
        return data


if __name__ == '__main__':
    Report3().report3()
