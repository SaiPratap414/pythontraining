subjects=["Maths","English","Science"]
marks=[40,70,20]

# Merging using zip as list of tuples
merged_list = list(zip(subjects, marks))
print("List of tuples:", merged_list)

# Merging using zip as dictionary
merged_dict = dict(zip(subjects, marks))
print("Dictionary:", merged_dict)
