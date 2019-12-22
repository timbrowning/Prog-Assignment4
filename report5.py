import sys
import pandas as pd
import datetime


class Report5:
    def report5(self,data):
        pd.set_option('display.max_columns', 10)
        print(data.sort_values(by=['year_of_bill', 'month_of_bill', 'day_of_bill'], ascending=False))
        input("Press Enter to display menu...\n")
        return


if __name__ == '__main__':
    Report5().report5()
