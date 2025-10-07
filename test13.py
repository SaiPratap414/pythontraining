flag = input("Enter the flag color (green, red, yellow): ")
match flag:
    case "green":
        print("Go")
    case "red":
        print("stop")
    case "yellow":
        print("slow down")
    case _:
        print("error")
    