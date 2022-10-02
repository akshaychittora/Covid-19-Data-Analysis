import json
import pandas as pd
import numpy as np


import datetime
df_cases=pd.read_csv('districts.csv')
df_coviddata=pd.read_csv('district_wise.csv')


districts= df_cases['District'].tolist()
states= df_cases['State'].tolist()

state_tocheck = df_coviddata['State'].tolist()
state_code= df_coviddata['State_Code'].tolist()
state_code_dict={}
for i in range(len(state_tocheck)):
    state_code_dict[state_tocheck[i]]=state_code[i]
district_code=[]
for i in range(len(districts)):
    district_code.append(state_code_dict[states[i]]+"_"+districts[i])


            
district_tocheck= df_coviddata['District'].tolist()
district_id= df_coviddata['District_Key'].tolist()


dates= df_cases['Date'].tolist()
cases=df_cases['Confirmed'].tolist()
temp=[]
def index(x,y):
    indices = []
    for i in range(len(districts)):
        if (districts[i] == x and states[i]==y):
            indices.append(i)
    return indices
index_dict={}

cases_dict={}
for i in range(len(districts)):
    if(districts[i]!='Unknown'):
        name= district_code[i]
        if(name not in cases_dict):
            indices= index(districts[i],states[i])
            
            temp1=[]
            for j in indices:
                temp1.append([dates[j], cases[j]])                
            cases_dict[name]=temp1


#weeks
new_districts=[]
new_time_id=[]
new_cases=[]
for i in cases_dict:
    for k in range(1,7):
        new_districts.append(i)
        new_time_id.append(k)
        new_cases.append(0)
    k=7
    pre=0
    for j in range(6,len(cases_dict[i]),7):
        datew=cases_dict[i][j][0]
        
        new_districts.append(i)
        new_time_id.append(k)
        k+=1
        new_cases.append(cases_dict[i][j][1]-pre)
        pre=cases_dict[i][j][1]


cases_week = {'districtid': new_districts,'timeid': new_time_id,'cases':new_cases}
df_ans3 = pd.DataFrame.from_dict(cases_week)
df_ans3.to_csv (r'cases-week.csv', index = False, header=True)

# ## months

new_districts2=[]
new_time_id2=[]
new_cases2=[]
for i in cases_dict:
    new_districts2.append(i)
    new_time_id2.append(1)
    new_cases2.append(0)
    k=2
    pre=0
    j=18
    while(j<len(cases_dict[i])):
        datew= int(cases_dict[i][j][0][-2:])

        while(datew!=14 and j< len(cases_dict[i])):
            j+=1
            string=cases_dict[i][j][0]
            datew = int(string[-2:])
            
        datew= int(cases_dict[i][j][0][-2:])
        if(datew==14):
            new_districts2.append(i)
            new_time_id2.append(k)
            k+=1
            new_cases2.append(cases_dict[i][j][1]-pre)
            pre=cases_dict[i][j][1]
        j+=28
            
cases_month = {'districtid': new_districts2,'timeid': new_time_id2,'cases':new_cases2}
df_ans3_2 = pd.DataFrame.from_dict(cases_month)
df_ans3_2.to_csv (r'cases-month.csv', index = False, header=True)
            

    
## overall
new_districts3=[]
new_time_id3=[]
new_cases3=[]
k=1
for i in cases_dict:
    new_districts3.append(i)
    new_time_id3.append(k)
    n= len(cases_dict[i])-1
    new_cases3.append(cases_dict[i][n][1])
cases_month = {'districtid': new_districts3,'timeid': new_time_id3,'cases':new_cases3}
df_ans3_3 = pd.DataFrame.from_dict(cases_month)
df_ans3_3.to_csv (r'cases-overall.csv', index = False, header=True)        

            
        
    




    
    
    
