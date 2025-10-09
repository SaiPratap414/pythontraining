def add(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    total = sum(args) + sum(kwargs.values())
    print("sum:", total)

add(4, 5, 3, 8, a=2, b=4, c=5)