## Q7

import json
import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta, date
import math
from dateutil import relativedelta

df_cowin=pd.read_csv('cowin_vaccine_data_districtwise (3).csv')
df_cowin=df_cowin.replace(np.nan, 0)



res= df_cowin['District_Key'].tolist()
district_key = []
for i in res:
    if (i not in district_key and i != 0):
        district_key.append(i)
        
output=[]
for i in district_key:
    value_cowin=df_cowin.loc[df_cowin['District_Key']==i]
    temp_list=[]
    temp_list.append(i)
    a= int(value_cowin['01-09-2021.9'].iloc[0])
    b=int(value_cowin['01-09-2021.8'].iloc[0])
    temp_list.append(a)
    temp_list.append(b)
    output.append(temp_list)
    
##district
list1=[]
list2=[]

for i in output:
    list1.append(i[0])
    a= i[1]
    
    b=i[2]
    if(b==0):
        list2.append(float('inf'))
    else:
        list2.append(float(a/b))

x = {'districtid': list1,'vaccineratio':list2}
df_ans7_1 = pd.DataFrame.from_dict(x)
df_ans7_1.to_csv (r'vaccinated-dose-ratio-district.csv', index = False, header=True)


## state
def match(x):
    string= x[:2]
    if(string in res1):
        return res2[res1.index(string)]

res2=[]
res1=[]
cowin_state=df_cowin['State'].tolist()
state_code=df_cowin['State_Code'].tolist()
for i in cowin_state:
    if (i not in res2 and i!=0):
        res2.append(i)
for i in state_code:
    if (i not in res1 and i!=0):
        res1.append(i)
list1=[]
list2=[]
for i in res2:
    covi=0
    covax=0
    for j in output:
        if(match(j[0])==i):
            covi+= j[1]
            covax+= j[2]
    list1.append(i)
    a= covi
    b=covax
    if(b==0):
        list2.append(float('inf'))
    else:
        list2.append(float(a/b))
        
y = {'stateid': list1,'vaccineratio':list2}
df_ans7_2 = pd.DataFrame.from_dict(y)
df_ans7_2.to_csv (r'vaccinated-dose-ratio-state.csv', index = False, header=True)
    
            
## overall

list1=[]
list2=[]
covi=0
covax=0
for i in output:
    covi+= i[1]
    covax+= i[2]
list1.append('india')
a= covi
b=covax
if(b==0):
    list2.append(float('inf'))
else:
    list2.append(float(a/b))
        
z = {'country': list1,'vaccineratio':list2}
df_ans7_3 = pd.DataFrame.from_dict(z)
df_ans7_3.to_csv (r'vaccinated-dose-ratio-overall.csv', index = False, header=True)
    

    
    

    
