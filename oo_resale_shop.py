from computer import *
class ResaleShop:
    #Attributes
    balance: float = 0.0
    inventory: list = []
    # Constructor
    def __init__(self, starting_balance: float) -> None:
         # You'll remove this when you fill out your constructor
        self.inventory = []
        self.balance = starting_balance
    # Methods
    #creates a computer and adds it to the inventory, removes price from balance
    def buy(self, name: str, price: float, year: int, OS: str, resale: float, memory: int):
        if self.balance>= price: 
            name = Computer(name, year, OS, resale, memory)
            self.inventory.append(name)
            self.balance-=price
            print("Computer Aquired!")
        else: 
            print("Insufficient Balance")
    #sells: adds the price to balance and removes the computer from the inventory
    def sell(self, computer):
        if computer in self.inventory: 
            self.balance+=computer.value
            self.inventory.remove(computer)
            print("Computer sold!")
        else:
            print("Computer does not exist")
    #updates, price, OS, and if the computer is too old, removes it from the inventory
    def refurbish(self, computer: Computer, newOS: str = None) -> None:
        if computer in self.inventory:
            if computer.year<2000:
                computer.value = 0.0
                self.inventory.remove(computer)
            elif computer.year<2012:
                computer.value = 250
            elif computer.year<2018: 
                computer.value = 550
            else: computer.value = 550
            if newOS is not None: 
                computer.opsystem= newOS 
        else: 
            print("Computer is not in inventory")
    #Updates the OS only
    def updateOS(self, computer: Computer, newOS: str):
        if computer in self.inventory: 
            computer.opsystem = newOS
        else: 
            print("computer does not exist")
    #Updates only the price
    def updatePrice(self, computer:Computer, newprice: float):
        if computer in self.inventory: 
            computer.value=newprice
        else:
            print("computer does not exist")
    #Prints inventory and the store balance
    def printInventory(self):
        for i in self.inventory:
            i.printDetails()
        print(self.balance)
def main():
    mystore = ResaleShop(500.00)
    mystore.buy("c1", 200.00, 2018, "OS10", 250.00, 120)
    c1=mystore.inventory[0]
    mystore.printInventory()
    mystore.refurbish(c1, "OS11")
    mystore.printInventory()
main()