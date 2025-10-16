from collections import UserList

users = UserList(["sai", "pratap", "chandu"])

class MyList(UserList):
    def pop(self, s=None):
        raise Exception("pop not allowed")  
        return
users = MyList(["sai", "pratap", "chandu"])
users.pop()