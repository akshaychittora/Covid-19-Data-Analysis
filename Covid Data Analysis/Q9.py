## Q9


import json
import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta, date
import math
from dateutil import relativedelta


df_census = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')
df_cowin=pd.read_csv('cowin_vaccine_data_districtwise (3).csv')
df_cowin=df_cowin.replace(np.nan, 0)

df_census['Name']=df_census['Name'].str.strip()
census_state=list(set(df_census['Name'].dropna()))
cowin_state=list(set(df_cowin['State'].dropna()))
cowin_state.remove(0)

out=[]
def date_conversion(x):
    return date(int(x[6:10]),int(x[3:5]),int(x[:2]))
def reverse_date(x):
    return x.strftime('%d-%m-%Y')
for i in cowin_state:
    for j in census_state:
        
        if(i.lower()==j.lower()):
            value_cowin=df_cowin.loc[df_cowin['State']==i]
            value_census= df_census.loc[df_census['Name']==j]
            tp= value_census['TOT_P'].iloc[0]
            temp=[]
            x=0
            y=0
            for k in range(len(value_cowin)):
                x+= int( value_cowin['14-08-2021.3'].iloc[k])
                y+=int(value_cowin['07-08-2021.3'].iloc[k])
            vaccinated= x-y
            temp.append(i)
            temp.append(tp-x)
            vaccination_rate= float(vaccinated/7)
            l=tp-x
            temp.append(vaccination_rate)
            days = math.ceil(float(l/vaccination_rate))
            new_date= date_conversion('14-08-2021')+timedelta(days)
            new_date=reverse_date(new_date)
            temp.append(new_date)
            out.append(temp)
        


tlist = list(zip(*out))
list1=tlist[0]
list2=tlist[1]
list3=tlist[2]
list4=tlist[3]
x = {'stateid': list1,'populationleft':list2,'rateofvaccination':list3,'date':list4}
df_ans9 = pd.DataFrame.from_dict(x)
df_ans9.to_csv (r'complete-vaccination.csv', index = False, header=True) 


        

