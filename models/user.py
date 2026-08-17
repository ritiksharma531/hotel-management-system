class User:
    def __init__(self, uid, name, mobile):
        self.uid = uid
        self.name = name
        self.mobile = mobile

    def __str__(self):
        return f"User {self.name} having uid {self.uid} has mobile {self.mobile}"