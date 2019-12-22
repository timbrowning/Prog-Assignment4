import sys
import pandas as pd
import datetime
import numpy as np


class Report7:
    def report7(self,data):
        pd.set_option('display.max_columns', 10)
        print("\n*********************Electric Ireland*********************************************")
        dfelectric = data[data['company_name'].str.contains("Electric Ireland")]
        dfelectric = dfelectric[['company_name', 'amount', 'credit_or_debit']]
        elec_total = dfelectric['amount'].sum()
        print(dfelectric)
        print("Electric Ireland is in ", elec_total, "Credit\n")
        print("**********************Energia*********************************************************")

        dfenergia = data[data['company_name'].str.contains("Energia")]
        dfenergia = dfenergia[['company_name', 'amount', 'credit_or_debit']]
        en_total = dfenergia['amount'].sum()
        print(dfenergia)
        print("Energia is in ", en_total, "Debit\n")
        print("**********************Vodafone******************************************************")

        dfvodafone = data[data['company_name'].str.contains("Vodafone")]
        dfvodafone = dfvodafone[dfvodafone['credit_or_debit'].str.contains("credit")]
        dfvodafone = dfvodafone[['company_name', 'amount', 'credit_or_debit']]
        vod_total_credit = dfvodafone['amount'].sum()

        dfvodafone = data[data['company_name'].str.contains("Vodafone")]
        dfvodafone = dfvodafone[dfvodafone['credit_or_debit'].str.contains("debit")]
        dfvodafone = dfvodafone[['company_name', 'amount', 'credit_or_debit']]
        vod_total_debit = dfvodafone['amount'].sum()
        final_vod = vod_total_credit - vod_total_debit

        dfvodafone = data[data['company_name'].str.contains("Vodafone")]
        dfvodafone = dfvodafone[['company_name', 'amount', 'credit_or_debit']]
        print(dfvodafone, "\n")
        print("Vodafone:",vod_total_credit, "Credit")
        print("Vodafone:",vod_total_debit, "Debit")
        print("Vodafone is in ", final_vod, "Debit\n")
        print("************************************************************************************************")
        input("Press Enter to display menu...\n")
        return


if __name__ == '__main__':
    Report7().report7()

#pd.to_datetime(rainfall_df[['year', 'month', 'day']])