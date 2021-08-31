import product
class Store:
    def __init__(self, name, prodList):
        self.name = name
        self.prodList = []

    def add_product(self, new_product):
        

    def sell_product(self, id):
        self.prodList.remove(id)

    def inflation(self, percent_increase):
        for prod in self.prodList:
            self.prodList[prod].update_price()

    def set_clearance(self, category, percent_discount):
        for prod in self.category:
            self.prodList[prod].update_price()



ipod = product.Product("iPod",400, "Music")
apple = Store("Apple", "Products")
apple.add_product(ipod)
print(apple.name)
print(apple.prodList)

ipod.update_price(0.02, True)
ipod.print_info()