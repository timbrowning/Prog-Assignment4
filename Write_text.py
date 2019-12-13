import sys
import pandas as pd
import datetime

class WriteToText:
    def to_text(self, data):
        data.to_csv(r'New.txt')
        print(data, "\n")
        print("The dataset \"results.csv\" has been added to a text file called \"New.txt\" ^")
        input("Press Enter to continue...\n")
        return


if __name__ == '__main__':
    WriteToText()