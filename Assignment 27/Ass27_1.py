class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        self.NoOfBooks = 0

    def increment_books(self):
        self.NoOfBooks += 1

    def Display(self):
        print(f"Name: {self.Name}, Author: {self.Author}, NoOfBooks: {self.NoOfBooks}")

#objects
BookStore1 = BookStore("Book1", "Author1")
BookStore1.increment_books()
BookStore1.Display()
