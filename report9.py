import sys
import pandas as pd
import datetime
import numpy as np


class Report9:
    def report9(self,data):

        data = pd.to_datetime(data[['year', 'month', 'day']])
        dif_list = []

        for i in range(len(data) - 1):
            dif_list.append((data[i] - data[i + 1]))
        print("\n****************Time Between Bills*****************************************")
        print(dif_list)
        avg = np.mean(dif_list)
        print("\n*******************Average Time between bills********************************************************")
        print("Average time between bills:", avg, "\n")
        input("Press Enter to display menu...\n")
        return


if __name__ == '__main__':
    Report9().report9()
