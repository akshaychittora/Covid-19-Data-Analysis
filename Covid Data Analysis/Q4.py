###Q4

import json
import pandas as pd
import numpy as np
from datetime import date


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

            
districts_peak=[]
cases_peak=[]
week_id_peak=[]

for i in cases_dict:
    date_begin=cases_dict[i][0][0]
    m=int(date_begin[5:7])
    date_b=int(date_begin[8:10])
    year=int(date_begin[:4])
    
    date1 = date(year,m,date_b)
    date2 = date(2020,3,15)
    days = abs(date1-date2).days
    po= ((days//14)*4)
    
    
    
    
    
    for l in range(1,po):
        districts_peak.append(i)
        cases_peak.append(0)
        week_id_peak.append(l)

    j=0
    pre=0
    w=po
    while(j<=len(cases_dict[i])-14):
        districts_peak.append(i)
        cases_peak.append(cases_dict[i][j+3][1]-pre)
        week_id_peak.append(w)
        w+=1
        
        districts_peak.append(i)
        cases_peak.append(cases_dict[i][j+6][1]-cases_dict[i][j][1])
        week_id_peak.append(w)
        w+=1
        
        districts_peak.append(i)
        cases_peak.append(cases_dict[i][j+10][1]-cases_dict[i][j+4][1])
        week_id_peak.append(w)
        w+=1
        
        districts_peak.append(i)
        cases_peak.append(cases_dict[i][j+13][1]-cases_dict[i][j+7][1])
        week_id_peak.append(w)
        w+=1
        pre=cases_dict[i][j+11][1]
        
        if(j==len(cases_dict[i])-14):
            districts_peak.append(i)
            cases_peak.append(cases_dict[i][j+13][1]-pre)
            week_id_peak.append(w)

        j+=14
    
        

        
distrcits_week_peak = {'districtid': districts_peak,'timeid': week_id_peak,'cases':cases_peak}
         


#peaks_month

districts_month_peak1=[]
month_id_peak=[]
month_cases_peak=[]
for i in cases_dict:
    date_begin=cases_dict[i][0][0]
    m=int(date_begin[5:7])
    date_c=int(date_begin[8:10])
    year=int(date_begin[:4])
    
    date1 = date(year,m,date_c)
    date2 = date(2020,int(date_begin[5:7])+1,14)
    days = abs(date1-date2).days
    po= int(date_begin[5:7])
    po= po- 3
    
    if(int(date_begin[8:10])<=14):
        po-=1
        j=0
    else:
        j=int(date_begin[8:10])+days
    
    for b in range(0,po):
        districts_month_peak1.append(i)
        month_id_peak.append(b)
        month_cases_peak.append(0)
    k=2
    pre=0
    while(j<len(cases_dict[i])):
        date_Z= int(cases_dict[i][j][0][-2:])

        while(date_Z!=14 and j< len(cases_dict[i])):
            
            string=cases_dict[i][j][0]
            date_Z = int(string[-2:])
            j+=1
        j-=1    
        date_Z= int(cases_dict[i][j][0][-2:])
        if(date_Z==14):
            districts_month_peak1.append(i)
            month_id_peak.append(k)
            k+=1
            month_cases_peak.append(cases_dict[i][j][1]-pre)
            pre=cases_dict[i][j][1]
        j+=28
            
districts_month_peak = {'districtid': districts_month_peak1,'timeid': month_id_peak,'cases':month_cases_peak}



districtid_peak=[]
wave1_weekid=[]
wave2_weekid=[]
wave1_monthid=[]
wave2_monthid=[]

ini= districts_peak[0]
index=0
j=0
initiate=0
i=0
while(i<len(districts_peak)):
    if(districts_peak[i]==ini):
        i+=1
    else:
        j=i
        n=j-initiate+1
        max1= cases_peak[initiate]
        index1=initiate
        max2=cases_peak[int(n/2)]
        index2=int(n/2)
        for y in range(initiate,initiate+int(n/2)):
            if(max1<cases_peak[y]):
                max1=cases_peak[y]
                index1=y
        for y in range(int(n/2)+initiate, j):
            if(max2<cases_peak[y]):
                max2=cases_peak[y]
                index2=y
        districtid_peak.append(ini)
        wave1_weekid.append(week_id_peak[index1])
        wave2_weekid.append(week_id_peak[index2])
        ini= districts_peak[i]
        i+=1
        initiate=i

i=0
ini= districts_month_peak1[0]
index=0
j=0
initiate=0
index_monthid1=0
index_monthid2=0
while(i<len(districts_month_peak1)):
    if(districts_month_peak1[i]==ini):
        i+=1
    else:
        j=i
        n=j-initiate+1
        max1= month_cases_peak[initiate]
        index1=initiate
        max2=month_cases_peak[int(n/2)]
        index2=int(n/2)
        index_monthid1=0
        index_monthid2=16
        for y in range(initiate,initiate+int(n/2)):
            if(max1<month_cases_peak[y]):
                max1=month_cases_peak[y]
                index1=y
        for y in range(int(n/2)+initiate, j):
            if(max2<month_cases_peak[y]):
                max2=month_cases_peak[y]
                index2=y
        
        wave1_monthid.append(month_id_peak[index1])
        wave2_monthid.append(month_id_peak[index2])
        ini= districts_month_peak1[i]
        i+=1
        initiate=i
wave1_monthid.append(index_monthid1)
wave2_monthid.append(index_monthid2)           
dist_peak = {'districtid': districtid_peak,'wave1_weeekid':wave1_weekid,'wave2_weekid':wave2_weekid,'wave1_monthid':wave1_monthid,'wave2_monthid':wave2_monthid}
df_ans4 = pd.DataFrame.from_dict(dist_peak)
df_ans4.to_csv (r'districts_peak.csv', index = False, header=True)            
            
        









