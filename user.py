class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country



if __name__ == "__main__":
    Bob = User("Bob", 15, "America") # Userクラスをインスタンス化 インスタンス=事実

    print(Bob) #<__main__.User object at 0x10cd1f390>
    print(Bob.name) # Bob
    print(Bob.age)
    print(Bob.country)

    Tom = User("Tom", 57, "canada")
    print(Tom)
    print(Tom.name)
    print(Tom.country)

    Ken = User("Ken", 49, "Japan")
    print(Ken)
    print(Ken.name)
    print(Ken.country)
