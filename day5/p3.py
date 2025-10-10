marks=[45,79,20,80]
result = [True if mark > 30 else False for mark in marks]
# for i in result:
#     if i!=True:
#         print("Fail")
#         break
# else:
#     print("Pass")
    
    
if all(result):
    print("pass")
else:
    print("fail")
