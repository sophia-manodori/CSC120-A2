class Computer:

    # Attributes
    id: int = 0
    year: int = 0
    opsystem: str = ""
    value: float = 0.0
    
    # Constructor
    def __init__(self, name: str, age: int, system:str, starting_price: float):
         # You'll remove this when you fill out your constructor
        self.id = name
        self.year = age
        self.opsystem = system
        self.value=starting_price
    # Methods
    #prints details
    def printDetails(self):
        print("Name:", self.id)
        print("OS:", self.opsystem)
        print("Year:", self.year)
        print("Price:", self.value)  

def main():
    apple = Computer("Apple", 2015, "OS11", 200.0)
    print(apple)
    apple.refurbish("OS12")
    print(apple.opsystem)