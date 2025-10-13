from datetime import datetime

d = datetime.now()
print(d)

# Use strptime to parse string to datetime
print(d.strftime("%B %d %Y"))