# subjects =["Maths", "English", "science"]
# counter=0
# for i in subjects:
#     counter = counter+1
#     #print(str(counter)+"."+i)
#     print(f"{counter}.{i}")
    
subjects = ["Maths", "English", "science"]
for id, subject in enumerate(subjects, start=2):
    print(f"{id}.{subject}")
