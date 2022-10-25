class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(User)
        
    def enroll(self):
        self.is_rewards_member = True
        if self.is_rewards_member == True:
            print("User is already a member")

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough gold card points- you currently have", (self.gold_card_points))
        else: self.gold_card_points = self.gold_card_points - amount
        print("You now have", (self.gold_card_points), "points")
            
    def add_points(self, points):
        self.gold_card_points = self.gold_card_points + points
        print("You now have", (self.gold_card_points), "points")

sophie = User("Sophie", "Slagle", "sl@gle.com", 28)

sophie.display_info()
sophie.enroll()
sophie.add_points(10)
sophie.spend_points(1)