class Product:
    def __init__(self, name, amount): # インスタンス変数
        self.name = name
        self.amount = amount

    def discount(self, price):
        self.amount -= price

    def innfulate(self, price):
        self.amount += price


# passは空っぽという意味


if __name__ == "__main__":
    p1 = Product("iPhone", 100000)  # プロダクトクラスのインスタンス化
    print(p1)
    print(p1.name)  # iPhone
    print(p1.amount)  # 100000
    p1.discount(5000)
    print(p1.amount)

    p2 = Product("MBA", 150000)
    print(p2.name)
    print(p2.amount)
    p2.discount(9500)
    print(p2.amount)
