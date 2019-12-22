import sys
import pandas as pd
import datetime


class Report4:
    def report4(self,data):

        print(data['company_name'].value_counts())

        input("Press Enter to display menu...\n")
        return


if __name__ == '__main__':
    Report4().report4()
