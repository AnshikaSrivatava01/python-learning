class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if not self.is_available:
            print(f"'{self.title}' is currently checked out.")
            return False
        self.is_available = False
        print(f"You borrowed '{self.title}'. Enjoy reading!")
        return True

    def return_book(self):
        if self.is_available:
            print(f"'{self.title}' was not borrowed; it is already in the library.")
            return False
        self.is_available = True
        print(f"'{self.title}' has been returned and is now available.")
        return True

    def status(self):
        state = "Available" if self.is_available else "Borrowed"
        print(f"'{self.title}' by {self.author} - Status: {state}")


book1 = Book("Clean Code", "Robert C. Martin")
book1.status()
book1.borrow_book()
book1.borrow_book()
book1.return_book()
book1.status()