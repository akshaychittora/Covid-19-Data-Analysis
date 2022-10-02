#Q5
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

districtid1=[]
weekid1=[]
dose1_1=[]
dose2_1=[]

df_cowin.fillna(0)
def date_conversion(x):
    return date(int(x[6:10]),int(x[3:5]),int(x[:2]))
def reverse_date(x):
    return x.strftime('%d-%m-%Y')
def isNaN(string):
    return string != string
for i in district_key:
    if(not isNaN(i)):
        value=df_cowin.loc[df_cowin['District_Key']==i]
        
        con_date= '16-01-2021'
        pre_dose1=int(value[con_date+".3"].iloc[0])
        pre_dose2=int(value[con_date+".4"].iloc[0])
        new_date= date_conversion(con_date)+timedelta(7)
        weekid=1
        limit= date(2021,9,1)
        while(new_date<=limit):
            date1=reverse_date(new_date)
            districtid1.append(i)
            weekid1.append(weekid)
            weekid+=1
            dose1_1.append(int(value[date1+".3"].iloc[0])-pre_dose1)
            pre_dose1=int(value[date1+".3"].iloc[0])
            dose2_1.append(int(value[date1+".4"].iloc[0])-pre_dose2)
            pre_dose2=int(value[date1+".4"].iloc[0])
            new_date=new_date+timedelta(7)
            
x = {'districtid': districtid1,'weekid': weekid1,'dose1':dose1_1,'dose2':dose2_1}
df_ans5_1 = pd.DataFrame.from_dict(x)
df_ans5_1.to_csv (r'district-vaccinated-count-week.csv', index = False, header=True) 
## months
districtid2=[]
monthid2=[]
dose1_2=[]
dose2_2=[]
for i in district_key:
    if(not isNaN(i)):
        value=df_cowin.loc[df_cowin['District_Key']==i]
        
        con_date= '16-01-2021'
        pre_dose1=int(value[con_date+".3"].iloc[0])
        pre_dose2=int(value[con_date+".4"].iloc[0])
        new_date= date_conversion(con_date)+relativedelta.relativedelta(months=1)
        monthid=1
        limit= date(2021,9,1)
        while(new_date<=limit):
            date1=reverse_date(new_date)
            districtid2.append(i)
            monthid2.append(monthid)
            monthid+=1
            dose1_2.append(int(value[date1+".3"].iloc[0])-pre_dose1)
            pre_dose1=int(value[date1+".3"].iloc[0])
            dose2_2.append(int(value[date1+".4"].iloc[0])-pre_dose2)
            pre_dose2=int(value[date1+".4"].iloc[0])
            new_date=new_date+relativedelta.relativedelta(months=1)
            
y = {'districtid': districtid2,'monthid': monthid2,'dose1':dose1_2,'dose2':dose2_2}
df_ans5_2 = pd.DataFrame.from_dict(y)
df_ans5_2.to_csv (r'district-vaccinated-count-month.csv', index = False, header=True) 


## overall
districtid3=[]
overall=[]
dose1_3=[]
dose2_3=[]
for i in district_key:
    value=df_cowin.loc[df_cowin['District_Key']==i]
    
    districtid3.append(i)
    overall.append(1)
    dose1_3.append(int(value['01-09-2021.3'].iloc[0]))
    dose2_3.append(int(value['01-09-2021.4'].iloc[0]))


z = {'districtid': districtid3,'overall': overall,'dose1':dose1_3,'dose2':dose2_3}
df_ans5_3 = pd.DataFrame.from_dict(z)
df_ans5_3.to_csv (r'district-vaccinated-count-overall.csv', index = False, header=True) 

            
            
### state wise            
## state wise
## week
a= df_cowin['State'].tolist()
b=df_cowin['State_Code'].tolist()
state_code = []
state=[]
for i in b:
    if (i not in state_code ):
        state_code.append(i)
for i in a:
    if (i not in state ):
        state.append(i) 
state.remove(0)
state_code.remove(0)
def state_name(x):
    string= x[:2]
    return a[b.index(string)]
        
stateid4=[]
weekid4=[]
dose1_4=[]
dose2_4=[]

for i in range(len(state)):
    temp_state=[state[i]]*32
    temp_week=[]
    for i in range(1,33):
        temp_week.append(i)
    temp_dose1=[0]*32
    temp_dose2=[0]*32
    for j in range(len(districtid1)):
        if(state_name(districtid1[j])==state[i]):
            #print(state[i])
            index= weekid1[j]-1
            temp_dose1[index]+= dose1_1[j]
            temp_dose2[index]+= dose2_1[j]
            
    stateid4= stateid4+ temp_state
    weekid4= weekid4+ temp_week
    dose1_4 = dose1_4 + temp_dose1
    dose2_4 = dose2_4 + temp_dose2
    

w = {'state': stateid4,'weekid': weekid4,'dose1':dose1_4,'dose2':dose2_4}
df_ans5_4 = pd.DataFrame.from_dict(w)
df_ans5_4.to_csv (r'state-vaccinated-count-week.csv', index = False, header=True)


## month
stateid5=[]
monthid5=[]
dose1_5=[]
dose2_5=[]


for i in range(len(state)):
    temp_state=[state[i]]*7
    temp_week=[]
    for i in range(1,8):
        temp_week.append(i)
    temp_dose1=[0]*7
    temp_dose2=[0]*7
    for j in range(len(districtid2)):
        if(state_name(districtid2[j])==state[i]):
            index= monthid2[j]-1
            temp_dose1[index]+= dose1_2[j]
            temp_dose2[index]+= dose2_2[j]
            
    stateid5= stateid5+ temp_state
    monthid5= monthid5+ temp_week
    dose1_5 = dose1_5 + temp_dose1
    dose2_5 = dose2_5 + temp_dose2
    

q = {'state': stateid5,'monthid': monthid5,'dose1':dose1_5,'dose2':dose2_5}
df_ans5_5 = pd.DataFrame.from_dict(q)
df_ans5_5.to_csv (r'state-vaccinated-count-month.csv', index = False, header=True)



#overall

stateid6=[]
overall6=[]
dose1_6=[]
dose2_6=[]


for i in range(len(state)):
    temp_state=[state[i]]*1
    temp_week=[]
    for i in range(1,2):
        temp_week.append(i)
    temp_dose1=[0]*1
    temp_dose2=[0]*1
    for j in range(len(districtid3)):
        if(state_name(districtid3[j])==state[i]):
            index= overall[j]-1
            temp_dose1[index]+= dose1_3[j]
            temp_dose2[index]+= dose2_3[j]
            
    stateid6= stateid6+ temp_state
    overall6= overall6+ temp_week
    dose1_6 = dose1_6 + temp_dose1
    dose2_6 = dose2_6 + temp_dose2
    

e = {'state': stateid6,'overall': overall6,'dose1':dose1_6,'dose2':dose2_6}
df_ans5_6 = pd.DataFrame.from_dict(e)
df_ans5_6.to_csv (r'state-vaccinated-count-overall.csv', index = False, header=True)



        
        
        
