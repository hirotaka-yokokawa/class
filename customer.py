class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        # return self.first_name + self.family_name
        return self.family_name + self.first_name

    def display_profile(self):
        print(f"Name: {self.full_name()}, Age: {self.age}")

    def display_full_name(self):
        print(self.full_name())


if __name__ == "__main__":
    tom = Customer("Tom", "Ford", 57)
    ken = Customer("Ken", "Yokoyama", 49)

    tom.display_profile()  # "Name: TomFord, Age: 57" と出力する
    ken.display_profile()

    ken.display_full_name()