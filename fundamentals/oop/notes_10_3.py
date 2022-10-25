# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
        
#     def greeting(self):
#         print(f"Hello, my name is {self.name}")

class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
        
    def on_sale_by_percentage(self, percent):
        self.price = self.price * (1-0.2)
        

skater_shoe = Shoe("Vans", "Low Tops", 59.99)
dress_shoe = Shoe("Boots", "Ballet Flats", 29.99)

skater_shoe.on_sale_by_percentage(0.2)
print(skater_shoe.price)

# print(skater_shoe.type)
# print(dress_shoe.type)


# def greeting(self):
#     print(f"Hello, I would like to buy {self.brand}")
    
# nike = Shoe("nike", "low", 69.99)
# nike.greeting()

# sophie = User("Sophie", "sla@soph.com")
# person = User("sarah", "sj@ksn.com")

# sophie.greeting()

# user_sophie = User()
# print(user_sophie.first_name)

# user_2 = User()
# print(user_2.first_name)