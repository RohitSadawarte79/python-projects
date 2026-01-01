'''
This program is just for practise I will be making an enventory of the items that you have now
name price quantity and methods how many items and methods to know items
inventory will have methods to add items 
to remove items and their quantity 
to view all items
search for an specific item and also their quantity
total price of all the items 
all the items will be stored inside an dictionary 
with this format 
dict = {
     item_name :{price : $, quantity: 1}
}

- first I will make the blueprint of the inventory and will write all it's methods 
- I will make an interface and work for it 

'''


class Inventory:

    database = {}

    def __init__(self , owner):
        self.owner = owner

    
    def add_item(self, item_name, item_price, item_quantity):
        item_name = item_name.lower()
        self.database[item_name] = {"price": item_price, "quantity" : item_quantity}

    def remove_item(self, item_name, item_quantity):
        item_name = item_name.lower()
        if item_name in self.database :
            quantity = self.database[item_name]["quantity"]
            price = self.database[item_name]["price"] / quantity
            if quantity < item_quantity:
                print(f"You only have {quantity} in stock. can't remove {item_quantity} from stock.")
                return 
            self.database[item_name]["quantity"] = quantity - item_quantity
            self.database[item_name]["price"] = (price * self.database[item_name]["quantity"])

            if self.database[item_name]["quantity"] != 0:
                return
            else:
                self.database.pop(item_name)

    def display_inventory(self):
        result = ""

        inventory = self.database

        for key , values in inventory.items():
            result += f"Item name: {key}. | Quantity: {values["quantity"]}. | Price: ${values["price"]}.\n"

        return result
    
    def search_item(self, item_name):
        if item_name in self.database:
            item = self.database[item_name]
            print(f"Item name: {item_name}. | Quantity: {item["quantity"]}. | Price: ${item["price"]}.\n")
        else:
            print("Item not found in the inventory. ")

    
    def total_price(self):
        cal = 0

        for key, value in self.database.items():
            cal += value["price"]
        
        return cal
    
    



def main():
    owner = input("Enter your name to create Inventory: ")
    inventory = Inventory(owner)
    print("Inventory created! \n")

    while True:

        

        print("Your Inventory: \n")

        print(inventory.display_inventory())

        print(f"total price: ${inventory.total_price()}.\n")

        print("Enter (add) to add item. \nEnter (remove) to remove item. \nEnter (quit) to quit. \nEnter (search) to search an specific item. \n")
        
        command = input("Write Your command: ")

        if command == "add":
            item = input("Enter item name: ")
            item_quantity = int(input("Enter quantity: "))
            item_price = int(input("Enter this item price for 1N: "))*item_quantity

            inventory.add_item(item, item_price, item_quantity)

        elif command == "remove":
            item = input("Enter item name to remove: ")
            item_quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(item, item_quantity)

        elif command == "quit":
            break

        elif command == "search":
            item = input("Enter item name to search: ")
            inventory.search_item(item)
        else:
            print("Invalid command do it again")
        
main()