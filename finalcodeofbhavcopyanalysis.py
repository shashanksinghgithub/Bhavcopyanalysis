# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:03:32 2021

@author: shashanks
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:15:52 2021

@author: shashanks
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:26:33 2021

@author: shashanks
"""

from zipfile import ZipFile
import pandas as pd 
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def unzip():
    #Unzipping the file
    zf = ZipFile('X:\New folder\cm14JAN221bhav.csv.zip', 'r')
    zf.extractall('X:\New folder\New folder')
    zf.close()
unzip()



#Adding a column for percentage change
df = pd.read_csv("X:\New folder\cm14JAN2021bhav.csv") 
df["PCRCHG"] = (df['CLOSE']-df['PREVCLOSE'])/df['PREVCLOSE'] *100
df.to_csv("X:\New folder\cm14JAN2021bhav.csv", index=False)


df = pd.read_csv("X:\New folder\cm14JAN2021bhav.csv") 

#Top 10 stocks wrt Total Traded Quantity
a = df.sort_values('TOTTRDQTY', ascending=False)[:10]
#Bottom 10 stocks wrt Total Traded Quantity
b = df.sort_values('TOTTRDQTY', ascending=True)[:10]
#Top 10 stocks wrt Percent change
c = df.sort_values('PCRCHG', ascending=False)[:10]
#Bottom 10 stocks wrt Percent change
d = df.sort_values('PCRCHG', ascending=True)[:10]

#Divide Total Traded Value in buckets of 500 cr
tottr1 = pd.Series(df['TOTTRDVAL']/10000000)
bins1 = (0, 500, 1000, 1500, 2000, 2500, 3000, 3500, np.inf)  # The edges
labels1 = ('0-500', '500-1000', '1000-1500', '1500-2000','2000-2500', '2500-3000', '3000-3500', '3500-4000' )
groups1 = pd.cut(tottr1, bins=bins1, labels=labels1)
trade_output = groups1.value_counts()
print(trade_output)

#Total Traded Value in buckets of 500 cr graph
trade_output.plot.bar()
plt.xlabel("Total traded values(in crore)", labelpad=14)
plt.ylabel("Number of companies)", labelpad=14)
plt.title("Total traded value of companies", y=1.02)
plt.savefig('X:\New folder\python_pretty_plot.png')
#Total Traded Value in buckets of 500 cr data
trade_outnam = groups1.value_counts().rename_axis('Total traded values(in crore)').reset_index(name='num_of_comp')

#Divide Percentage change in buckets of 1% 
pcr2 = pd.Series(df['PCRCHG'])
bins2 = (-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
labels2 = ('-20-19','-19-18','-18-17', '-17-16', '-16-15','-15-14', '-14-13', '-13-12', '-12-11', '-11-10', '-10-9', '-9-8', '-8-7', '-7-6', '-6-5', '-5-4', '-4-3', '-3-2', '-2-1', '-1-0', '0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20')
groups2 = pd.cut(pcr2, bins=bins2, labels=labels2)
change_output = groups2.value_counts()
print(change_output)

#Percentage change in buckets of 1% graph 
change_output.plot.bar()
plt.xlabel("Percentage of change", labelpad=14)
plt.ylabel("Number of companies", labelpad=14)
plt.title("Percentage of change in companies price", y=1.02);
plt.savefig('X:\New folder\change_plot.png')
#Percentage change in buckets of 1% data
trade_outper = groups2.value_counts().rename_axis('Percentage of change').reset_index(name='num_of_comp')


#appending all dataframe and plot png to excel sheet and providing them with title
with pd.ExcelWriter('X:\New folder\New folder\G2.xlsx') as writer:
    a.to_excel(writer, sheet_name='sheet1',startrow=4 , startcol=0)      
    b.to_excel(writer, sheet_name='sheet1',startrow=20 , startcol=0)
    c.to_excel(writer, sheet_name='sheet1',startrow=40 , startcol=0)
    d.to_excel(writer, sheet_name='sheet1',startrow=60 , startcol=0)
    trade_outnam.to_excel(writer, sheet_name='sheet1',startrow=80 , startcol=0)
    trade_outper.to_excel(writer, sheet_name='sheet1', startrow=100 , startcol=0)
    sheet = writer.sheets['sheet1'] #change this to your own
    sheet.write(0,0,'Top 10 stocks wrt Total Traded Quantity')
    sheet.write(18,0, 'Bottom 10 stocks wrt Total Traded Quantity')
    sheet.write(38,0, 'Top 10 stocks wrt Percent change')
    sheet.write(58,0, 'Bottom 10 stocks wrt Percent change')
    sheet.write(78,0, 'Total Traded Value in buckets of 500cr')
    sheet.write(98,0, 'Percentage change in buckets of 1% ')
    sheet.insert_image(78,6, 'X:\New folder\python_pretty_plot.png')
    sheet.insert_image(118,6, 'X:\New folder\change_plot.png')

    writer.save()

