import sys
import pandas as pd
import datetime
import numpy as np


class Report8:
    def report8(self,data):
        data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
        switch = 1
        while switch == 1:
            start_date = input("Press Enter Start Date?\n")
            try:
                start_date = pd.to_datetime(start_date)
                switch = 0
            except ValueError:
                print('Unrecognized date format, please try again')
                input("Press Enter to try again...\n")

        switch2 = 1
        while switch2 == 1:
            end_date = input("Press Enter End Date?\n")
            try:
                end_date = pd.to_datetime(end_date)
                switch2 = 0
            except ValueError:
                print('Unrecognized date format, please try again')
                input("Press Enter to try again...\n")

        mask = (data['date'] > start_date) & (data['date'] <= end_date)
        print(data[mask], "\n")
        print("*********************************************************")
        print("Average spent between two times is:", data[mask]['amount'].mean())
        print("*********************************************************\n")

        input("Press Enter to display menu...\n")
        return


if __name__ == '__main__':
    Report8().report8()
