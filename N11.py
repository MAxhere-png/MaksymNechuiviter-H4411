class Product:
    def __init__(self,name, price,):
        self.name = name
        self.price = price
        self.is_available = False

    def mark_as_available(self):
        self.is_available = True

    def __str__(self):
        status = "Додано" if self.is_available else "Не додано"
        return f"[{status}] {self.name}"

class Cart:
    def __init__(self):
        self.products = []

    def add_to_cart(self, name, price):
        new_product = Product(name, price)
        self.products.append(new_product)
        print(f"Товар '{name}' додано")

    def delete_product(self, name):
        self.products = [product for product in self.products if product.name != name ]
        print(f"Товар '{name}'' видалено")

    def mark_product_available(self,name):
        for product in self.products:
            if product.name == name:
                product.mark_as_available()
                print("Товар", product, "доступний для придбання")
                return
        print(f"Товар не знайдено")
    def list_cart(self):
        if not self.products:
            print("Ваша корзина товарів порожня")
        else:
            print("\nВаша корзина товарів:",)
            for product in self.products:
                print(product)

user_cart = Cart()
user_cart.add_to_cart("Велосипед", "Фігурка ігрового персонажу" )
user_cart.mark_product_available("Велосипед")
user_cart.list_cart()
