from collections import Counter
EmpLocation = ['Hyd', 'Bang', 'Chennai', 'pune', "Hyd", "pune", "Hyd"]
location_counts = Counter(EmpLocation)
print(location_counts)
print(location_counts.most_common(2))  # Top 2 most common locations
