class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# passは空っぽという意味


if __name__ == "__main__":
    p1 = Product("iPhone", 100000)  # プロダクトクラスのインスタンス化
    print(p1)
    print(p1.name)  # iPhone
    print(p1.price)  # 100000

    p2 = Product("MBA", 150000)
    print(p2.name)
    print(p2.price)
