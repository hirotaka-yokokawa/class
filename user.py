class User:
    def __init__(self, name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):
        # display_profile() は Userクラスの インスタンスメソッド
        print(f"私は{self.name}です｡国籍は{self.country}の{self.age}歳です｡")

    def change_nationality(self,country_name):
        self.country = country_name


if __name__ == "__main__":
    Bob = User("Bob", 15, "USA") # Userクラスをインスタンス化 インスタンス=事実
    Bob.display_profile()
    Bob.change_nationality("China")
    Bob.display_profile()

    Tom = User("Tom", 57, "USA")
    Tom.display_profile()
    Tom.change_nationality("UK")
    Tom.display_profile()

    Ken = User("Ken", 49, "Jp")
    Ken.display_profile()
    Ken.change_nationality("In")
    Ken.display_profile()
