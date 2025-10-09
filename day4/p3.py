dict1 ={"a":1,"b":2}
dict2 ={"b":3,"c":4}

dict3 = dict1.copy()
for key,value in dict2.items():
    dict3[key] =dict3.get(key,0)+ value
print (dict3)