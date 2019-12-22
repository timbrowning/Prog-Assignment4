import sys
import pandas as pd
import datetime
import numpy as np


class Report6:
    def report6(self,data):
        dfcredit = data[data['credit_or_debit'].str.contains("credit")]
        dfdebit = data[data['credit_or_debit'].str.contains("debit")]
        print(dfcredit.loc[dfcredit['amount'].idxmax()], '\n')
        print(dfdebit.loc[dfdebit['amount'].idxmax()])
        input("Press Enter to display menu...\n")
        return


if __name__ == '__main__':
    Report6().report6()
