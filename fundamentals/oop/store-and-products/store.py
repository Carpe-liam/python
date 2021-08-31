import product
class Store:
    def __init__(self, name, prodList):
        self.name = name
        self.prodList = []

    def add_product(self, new_product):
        self.new_product = new_product
        self.prodList.append(new_product)

    def sell_product(self, id):
        self.id = id
        self.prodList.remove(id)
        print(f"{id.name} sold for {id.price}.")
        print("-"*50)

    def inflation(self, percent_increase):
        for product in self.prodList:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.prodList:
            if product.category == category:
                product.update_price(percent_discount, False)

    def print_product(self):
        print("Welcome to Apple! Here are our current products:")
        for product in self.prodList:
            print(f"{product.name} - ${product.price}. | Caterogy: {product.category}")
        print("~"*60)

### WORKING ###
ipod = product.Product("iPod",400, "Music")
ipad = product.Product("iPad", 900, "Productivity")
apple = Store("Apple", "Products")
ipod.update_price(0.02, True)
apple.add_product(ipod)
apple.add_product(ipad)
apple.print_product()

apple.set_clearance("Music", 0.2)
apple.print_product()

apple.sell_product(ipod)
apple.print_product()

apple.inflation(0.1)
apple.print_product()
