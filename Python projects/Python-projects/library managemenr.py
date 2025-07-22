class library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")
        self.no_of_books += 1
    def get_numbers_of_books(self):
      return self.no_of_books

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")
    def list_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")

print("Library Management System")
lib = library()
while True:
    print("\nOptions:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. List Books")
    print("4. no.of books")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        book_name = input("Enter the name of the book to add: ")
        lib.add_book(book_name)
    elif choice == '2':
        book_name = input("Enter the name of the book to remove: ")
        lib.remove_book(book_name)
    elif choice == '3':
        lib.list_books()
    elif choice == '4':
        print("Total number of books:", lib.get_numbers_of_books())
    elif choice == '5': 

        print("Exiting the library management system.")
        break
    else:
        print("Invalid choice, please try again.")

# This code implements a simple library management system that allows users to add, remove, and list books in the library.
# It also provides the total number of books in the library.

