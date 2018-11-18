class User:
    def __init__(self, name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country



if __name__ == "__main__":
    Bob = User("Bob", 15, "America") # Userクラスをインスタンス化 インスタンス=事実

    Tom = User("Tom", 57, "canada")

    Ken = User("Ken", 49, "Japan")
