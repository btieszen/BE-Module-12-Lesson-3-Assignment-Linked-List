#Implementing a Singly Linked List in Python

class Movie:
   def __init__ (self,title,rating,year):
        self.title = title
        self.rating = rating
        self.year = year
        
class Node:
    def __init__ (self,movie):
        self.movie = movie
        self.next = None
      
class SinglyLinkedList: 
    def __init__ (self):
        self.head = None
        self.tail = None
        
    def add_movie(self,title,rating,year):
        new_movie = Movie(title,rating, year)
        new_node = Node(new_movie)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    
    def delete_movie(self,title):
        current = self.head
        while current:
            if current.movie.title == title:
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
    
    def traverse_movielist(self):
        if not self.head:
            print("Movie list is empty")
            return
        current = self.head
        while current:
            print(f"Tile: {current.movie.title}")
            print(f"Rating: {current.movie.rating}")
            print(f"Year: {current.movie.year}")
            print("---------------------------")
            current = current.next
            
playlist_manager =SinglyLinkedList()

playlist_manager.add_movie("Star wars","PG-13",1977)
playlist_manager.add_movie("Shrek","G",2001)
playlist_manager.add_movie("Cujo","R",1983)

playlist_manager.delete_movie("Shrek")
playlist_manager.traverse_movielist()

        