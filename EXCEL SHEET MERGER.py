# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 01:41:25 2023

@author: linto
"""
import glob
import pandas as pd
 

path = "C:/Users/linto/.spyder-py3/MERGER/"
 
# csv files in the path
file_list = glob.glob(path + "/*.xlsx")
 
a =[]
for file in file_list:
    
    a.append(file)  
    print(file)
        
 
print(a)
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel(a[0])

 
#print(dataframe1)
print(dataframe1.iloc[:,[0]])

si = dataframe1.size

b = []
print(si)
for i in range(int(si/2)):
    b.append(dataframe1.iloc[i,0])   
print('list hai yeh')   
print(b) 

path = a[0]

for i in range(len(b)):

    for j in range(len(a)):
        
        if('C:/Users/linto/.spyder-py3/MERGER\\'+str(b[i])+'.xlsx'== a[j]):
            print('C:/Users/linto/.spyder-py3/MERGER\\'+str(b[i])+'.xlsx'== a[j])
            path1 = a[j]
            df = pd.read_excel(path1)
            print(df)
            writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
            dataframe1.to_excel(writer, sheet_name = 'x1') 
            df.to_excel(writer, sheet_name = 'x3')
            writer.close() 
            break
        else:
            print('not found 404')


#dataframe1_total = dataframe1_total.append(df)
#df_total.to_excel('combined_file.xlsx')  
