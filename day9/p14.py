from collections import ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {'d': 5, 'e': 6}
d4 = {'f': 7, 'g': 8}

d = ChainMap(d1, d2, d3, d4)
for key in d:
    print(f"{key}: {d[key]}")
print(d)
print(d.maps)  # List of dictionaries in the ChainMap