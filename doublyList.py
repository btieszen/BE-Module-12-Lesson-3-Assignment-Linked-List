#Implementing a Doubly Linked List in Python

class Cars: # this is our data
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
   
        
class Node: 
    def __init__ (self,cars):
        self.cars = cars
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        
    def add_cars(self,make,model,year):
        new_cars = Cars(make,model,year)
        new_node = Node(new_cars)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    
    def delete_cars(self,make):
        current = self.head
        while current:
            if current.cars.make == make:
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False
    
    def traverse_cars(self):
        if not self.head:
            print("NO cars in inventory")
            return
        current = self.head
        while current:
            print(f"Make: {current.cars.make}")
            print(f"Model: {current.cars.model}")
            print(f"Year: {current.cars.year}")
            print("---------------------------")
            current = current.next
            
inventory_cars =DoublyLinkedList()

inventory_cars.add_cars("Ford","Mustang",2020)
inventory_cars.add_cars("Chevrolet","corvette",2024)
inventory_cars.add_cars("Honda","Accord",2023)
inventory_cars.add_cars("Toyota","Corolla",2020)

print('')
print("Current Cars in Inventory:\n")
inventory_cars.delete_cars("Ford")


inventory_cars.traverse_cars()
