customer = {"name":"Sai","city":"Bangalore","score":100}
# print(customer["age"])
print(customer.get("age", 24))
print(customer.get("name"))
print(customer)
customer["name"] = "pratap"
print(customer)
customer["state"] = "karnataka"
print(customer)
customer["score"]= customer.get("score",0)+1
print(customer)
del customer["city"]
print(customer)