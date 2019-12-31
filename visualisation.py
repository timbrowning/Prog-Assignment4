import sys
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def vis_report3(data):
    group2 = data.groupby(['year', 'credit_or_debit'])['amount'].agg('sum')
    print(group2)
    groups2 = group2.sort_values(axis=[0][0], ascending=False)
    group2.plot.bar(color="blue")
    plt.show()

def vis_report4(data):
    group = data['company_name'].value_counts()
    group.plot.bar(color="red")
    plt.show()

def vis_report5(data):
    data = data.sort_values(by=['year', 'month', 'day'], ascending=False)
    data = data[['company_name', 'year']]
    data.plot(x='company_name', kind = 'bar', color="purple")
    plt.xlabel('company_name')
    plt.ylim(2015, 2020)
    plt.show()

def vis_report6(data):
    data = data.sort_values(by=['amount'])
    data.plot(x='company_name' , y="amount", kind='bar')
    plt.show()

def vis_report7(data):
    dfelectric = data[data['company_name'].str.contains("Electric Ireland")]
    elec_total = dfelectric['amount'].sum()
    dfelectric = dfelectric.plot(x='company_name', y="amount", kind='bar')
    dfelectric.set_ylabel(elec_total, fontsize=12)

    dfenergia = data[data['company_name'].str.contains("Energia")]
    en_total = dfenergia['amount'].sum()
    dfenergia = dfenergia.plot(x='company_name', y="amount", kind='bar')
    dfenergia.set_ylabel(en_total, fontsize=12)

    dfvodafone = data[data['company_name'].str.contains("Vodafone")]
    dfvodafone = dfvodafone[dfvodafone['credit_or_debit'].str.contains("credit")]
    vod_total_credit = dfvodafone['amount'].sum()

    dfvodafone = data[data['company_name'].str.contains("Vodafone")]
    dfvodafone = dfvodafone[dfvodafone['credit_or_debit'].str.contains("debit")]
    vod_total_debit = dfvodafone['amount'].sum()
    final_vod = vod_total_credit - vod_total_debit

    dfvodafone = dfvodafone.plot(x='company_name', y="amount", kind='bar')
    dfvodafone.set_ylabel(final_vod, fontsize=12)

    plt.show()

def vis_report8(data):
    dates = pd.to_datetime(data[['year', 'month', 'day']])
    amount = data['amount']
    plt.plot_date(dates, amount)
    plt.show()


if __name__ == '__main__':
   data = pd.read_csv("results.csv",
                       names=['company_name', 'customer_name', 'year', 'month', 'day',
                              'amount', 'credit_or_debit'])

   vis_report3(data)
   vis_report4(data)
   vis_report5(data)
   vis_report6(data)
   vis_report7(data)
   vis_report8(data)