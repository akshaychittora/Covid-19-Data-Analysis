### Q1

import json
import pandas as pd
import numpy as np


data = json.loads(open('neighbor-districts.json').read())

new_dict={}
for i in data:
    if('_district' in i ):
        k=i[:i.index('_')]
    else:
        k=i[:i.index('/')]
    v_list=[]
    for j in data[i]:
        if('_district' in j ):
            l=j[:j.index('_')]
        else:
            l=j[:j.index('/')]
        v_list.append(l)
    new_dict[k]=v_list
    
    
df_vaccine=pd.read_csv('cowin_vaccine_data_districtwise (1).csv')
df_covid=pd.read_csv('district_wise.csv')
vaccine_dist=[]

vaccine_dist = df_vaccine["District"].tolist()
covid_dist= df_covid['District'].tolist()
vaccine_distkey= df_vaccine['District_Key'].tolist()


for i in range(1,len(vaccine_dist)):
    vaccine_dist[i]=vaccine_dist[i].replace(" ","_")
    vaccine_dist[i]=vaccine_dist[i].lower()
    
for i in range(len(covid_dist)):
    covid_dist[i]=covid_dist[i].lower()
    
    
update= {}
for i in list(new_dict):
    if(i in vaccine_dist):
        for j in list(new_dict[i]):
            #print(j)
            if(j not in vaccine_dist):
                new_dict[i].remove(j)
        ind= vaccine_dist.index(i)
        key=vaccine_distkey[ind]
        #print(key)
        new_dict[key] = new_dict.pop(i)
        update[i]=key
    else:
        new_dict.pop(i)
        
        
for i in new_dict:
    for j in range(len(new_dict[i])):
        new_dict[i][j]=update[new_dict[i][j]]
        
new_dict=(dict(sorted(new_dict.items())))
with open('neighbor-districts-modified.json', 'w') as fp:
    json.dump(new_dict, fp, sort_keys=True, indent=4)