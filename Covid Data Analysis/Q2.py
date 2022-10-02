### Q2
import json
import pandas as pd
import numpy as np

data2 = json.loads(open('neighbor-districts-modified.json').read())
list1=[]
list2=[]

for i in data2:
    for j in data2[i]:
        list1.append(i)
        list2.append(j)
        if(i in data2[j]):
            data2[j].remove(i)       

ans_dict={'district': list1, 'neighbour': list2}
df_ans = pd.DataFrame.from_dict(ans_dict)
df_ans.to_csv (r'edge-graph.csv', index = False, header=True)