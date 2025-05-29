
mcDonalds_base_items = {"10-piece McNuggets": 4.99, "McDouble": 4.79,
                        "McChicken": 4.39, "Coca-Cola": 2.23,
                        "Sausage Biscuit": 4.79, "Sausage Burrito": 3.99,
                        "McCrispy": 7.09, "Filet-O-Fish": 6.99,
                        "Cheeseburger": 4.09, "Double Cheeseburger": 5.09,
                        "Big Mac": 7.89, "Hamburger": 3.59, "Quarter Pounder": 7.99,
                        "Small Fries": 1.89, "Medium Fries": 3.29, "Large Fries": 3.79}
user_preferences = []

budget = float(input("How much money do you have to spend at McDonalds: "))
print("Please rank the following items in how much you like them from 0-100")
for item in mcDonalds_base_items.keys():

    item_value = int(input(f"{item}: "))
    user_preferences.append(item_value)

print(user_preferences)