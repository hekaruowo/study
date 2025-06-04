
class user():

    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password

    def print_user(self):
        print(self.name, self.age, self.password)
user1 = user("John", 22, "password")
user1.print_user()