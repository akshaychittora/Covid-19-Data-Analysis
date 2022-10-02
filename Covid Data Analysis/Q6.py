## Q6
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

df_census_new= df_census[['Level','Name','TRU','TOT_M','TOT_F']].copy()

df_census_new['Name']=df_census_new['Name'].str.strip()
df_census_new.head()
census_dist=list(set(df_census_new['Name'].dropna()))
cowin_dist= list(set(df_cowin['District'].dropna()))
cowin_state=df_cowin['State'].tolist()
changes={
    'Mahbubnagar':'Mahabubnagar',
    'Rangareddy':'Ranga Reddy',
    'Sri Potti Sriramulu Nellore':'S.P.S. Nellore',
    'Y.S.R.':'Y.S.R. Kadapa',
    'Dibang Valley':'Upper Dibang Valley',
    'Kaimur (Bhabua)':'Kaimur',
    'Pashchim Champaran':'West Champaran',
    'Purba Champaran':'East Champaran',
    'Janjgir - Champa':'Janjgir Champa',
    'Ahmadabad':'Ahmedabad',
    'Banas Kantha':'Banaskantha',
    'Dohad':'Dahod',
    'Kachchh':'Kutch',
    'Mahesana':'Mehsana',
    'Panch Mahals':'Panchmahal',
    'Sabar Kantha':'Sabarkantha',
    'The Dangs':'Dang',
    'Lahul & Spiti':'Lahaul & Spiti',
    'Gurgaon':'Gurugram',
    'Mewat':'Nuh',
    'Kodarma':'Koderma',
    'Pashchimi Singhbhum':'West Singhbhum',
    'Purbi Singhbhum':'East Singhbhum',
    'SaraikelaKharsawan':'',
    'Badgam':'Budgam',
    'Bandipore':'Bandipora',
    'Baramula':'Baramulla',
    'Shupiyan':'Shopiyan',
    'Bagalkot':'Bagalkote',
    'Bangalore':'Bengaluru',
    'Bangalore Rural':'Bengaluru Rural',
    'Belgaum':'Belagavi',
    'Bellary':'Ballari',
    'Bijapur':'Vijayapura',
    'Chamarajanagar':'Chamarajanagara',
    'Chikmagalur':'Chikkamagaluru',
    'Gulbarga':'Kalaburagi',
    'Mysore':'Mysuru',
    'Shimoga':'Shivamogga',
    'Tumkur':'Tumakuru',
    'Ahmadnagar':'Ahmednagar',
    'Bid':'Beed',
    'Buldana':'Buldhana',
    'Gondiya':'Gondia',
    'Khandwa (East Nimar)':'Khandwa',
    'Khargone (West Nimar)':'Khargone',
    'Narsimhapur':'Narsinghpur',
    'Anugul':'Angul',
    'Baleshwar':'Balasore',
    'Baudh':'Boudh',
    'Debagarh':'Deogarh',
    'Jagatsinghapur':'Jagatsinghpur',
    'Jajapur':'Jajpur',
    'Firozpur':'Ferozepur',
    'Muktsar':'Sri Muktsar Sahib',
    'Sahibzada Ajit Singh Nagar':'S.A.S. Nagar',
    'Chittaurgarh':'Chittorgarh',
    'Dhaulpur':'Dholpur',
    'Jalor':'Jalore',
    'Jhunjhunun':'Jhunjhunu',
    'Kanniyakumari':'Kanyakumari',
    'The Nilgiris':'Nilgiris',
    'Allahabad':'Prayagraj',
    'Bara Banki':'Barabanki',
    'Faizabad':'Ayodhya',
    'Jyotiba Phule Nagar':'Amroha',
    'Kanshiram Nagar':'Kasganj',
    'Kheri':'Lakhimpur Kheri',
    'Mahamaya Nagar':'Hathras',
    'Mahrajganj':'Maharajganj',
    'Sant Ravidas Nagar (Bhadohi)':'Bhadohi',
    'Garhwal':'Pauri Garhwal',
    'Hardwar':'Haridwar',
    'Darjiling':'Darjeeling',
    'Haora':'Howrah',
    'Hugli':'Hooghly',
    'Koch Bihar':'Cooch Behar',
    'Maldah':'Malda',
    'North Twenty Four Parganas':'North 24 Parganas',
    'Puruliya':'Purulia',
    'South Twenty Four Parganas':'South 24 Parganas'
}

out=[]
left=[]
for i in census_dist:
    if(i in cowin_dist):
        
        value_cowin=df_cowin.loc[df_cowin['District']==i]
        
        value_census= df_census.loc[df_census['Name']==i]
        if(len(value_cowin)!=0 and len(value_census)!=0):
            state= value_cowin['State'].iloc[0]
            districtid=value_cowin['District_Key'].iloc[0]
            total_m_v= int(value_cowin['01-09-2021.5'].iloc[0])
            total_f_v= int(value_cowin['01-09-2021.6'].iloc[0])
            total_m= int(value_census['TOT_M'].iloc[0])
            total_f=int(value_census['TOT_F'].iloc[0])
            out.append((state,districtid,total_m_v,total_f_v,total_m,total_f))
    if(i not in cowin_dist):
        left.append(i)
        

for i in left:
    if(i in changes):
        value_cowin=df_cowin.loc[df_cowin['District']==changes[i]]
        
        value_census= df_census.loc[df_census['Name']==i]
        if(len(value_cowin)!=0 and len(value_census)!=0):
            state= value_cowin['State'].iloc[0]
            districtid=value_cowin['District_Key'].iloc[0]
            total_m_v= int(value_cowin['01-09-2021.5'].iloc[0])
            total_f_v= int(value_cowin['01-09-2021.6'].iloc[0])
            total_m= int(value_census['TOT_M'].iloc[0])
            total_f=int(value_census['TOT_F'].iloc[0])
            out.append((state,districtid,total_m_v,total_f_v,total_m,total_f))
        

   
output_district=[]
#district wise
for i in out:
    temp_list=[]
    temp_list.append(i[1])
    a=float(i[3]/i[2])
    temp_list.append(a)
    b=float(i[5]/i[4])
    temp_list.append(b)
    temp_list.append(float(a/b))
    output_district.append(temp_list)

output_state=[]
res=[]
for i in cowin_state:
    if (i not in res and i!=0):
        res.append(i)

for i in res:
    temp_list=[]
    tmv=0
    tfv=0
    tm=0
    tf=0
    
    for j in out:
        if(j[0]==i):
            tmv+=j[2]
            tfv+=j[3]
            tm+=j[4]
            tf+=j[5]
    
    temp_list.append(i)
    if(tmv==0):
        a=float('inf')
    else:
        a= float(tfv/tmv)
    temp_list.append(a)
    if(tm==0):
        b=float('inf')
        
    else:
        b= float(tf/tm)
    temp_list.append(b)
    temp_list.append(float(a/b))
    output_state.append(temp_list)
    
output_overall=[]
tmv=0
tfv=0
tm=0
tf=0
for i in out:
    tmv+=i[2]
    tfv+=i[3]
    tm+=i[4]
    tf+=i[5]
if(tmv==0):
    a=float('inf')
else:
    a= float(tfv/tmv)
if(tm==0):
    b=float('inf')    
else:
    b= float(tf/tm)
list1=[]
list2=[]
list3=[]
list4=[]
list1.append('India')
list2.append(a)
list3.append(b)
list4.append(float(a/b))
z ={'country': list1,'vaccinationratio':list2,'populationratio':list3,'ratioofratios': list4}
df_ans6_3 = pd.DataFrame.from_dict(z)
df_ans6_3.to_csv (r'vaccination-population-ratio-overall.csv', index = False, header=True)  


output_district.sort(key=lambda x: x[3],reverse=False)
tlist = list(zip(*output_district))
list1=tlist[0]
list2=tlist[1]
list3=tlist[2]
list4=tlist[3]
x = {'districtid': list1,'vaccinationratio':list2,'populationratio':list3,'ratioofratios': list4}
df_ans6_1 = pd.DataFrame.from_dict(x)
df_ans6_1.to_csv (r'vaccination-population-ratio-district.csv', index = False, header=True) 



output_state.sort(key=lambda x: x[3],reverse=False)
tlist1 = list(zip(*output_state))
list1=tlist1[0]
list2=tlist1[1]
list3=tlist1[2]
list4=tlist1[3]
y = {'districtid': list1,'vaccinationratio':list2,'populationratio':list3,'ratioofratios': list4}
df_ans6_2 = pd.DataFrame.from_dict(y)
df_ans6_2.to_csv (r'vaccination-population-ratio-state.csv', index = False, header=True) 
