#a = 10
try:
    print(a)
except NameError:
    print("Variable 'a' is not defined")
else:
    print("Variable 'a' is defined and accessible") 
finally:
    print("Execution completed")