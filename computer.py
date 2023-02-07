class Computer:

    # Attributes
    id: str = ""
    year: int = 0
    opsystem: str = ""
    value: float = 0.0
    memory: int = 0
    
    # Constructor
    def __init__(self, name: str, age: int, system:str, starting_price: float, memory: int):
         # You'll remove this when you fill out your constructor
        self.id = name
        self.year = age
        self.opsystem = system
        self.value=starting_price
        self.memory = memory
    # Methods
    #prints details
    def printDetails(self):
        print("Name:", self.id)
        print("OS:", self.opsystem)
        print("Memory:", self.memory)
        print("Year:", self.year)
        print("Price:", self.value)  
def main():
    apple = Computer("Apple", 2015, "OS11", 200.0)
    print(apple)
    apple.refurbish("OS12")
    print(apple.opsystem)