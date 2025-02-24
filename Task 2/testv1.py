import pyodbc
server='MJOLNER'
database='task_2'

cnxn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                    SERVER='+ server + '; \
                    DATABASE=' + database +';\
                    Trusted_connection=yes;'
    )
cursor=cnxn.cursor()

def show_menu():
    print('CHOOSE OPTIONS\n' '   1: Register user\n''   2: Show Books\n''   3: Show book details\n''   4: UPDATE NOTE\n''   5: DELETE NOTE\n''   Q: QUIT THE APPLICATION\n''   M:SHOW MENU')



class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{self.title} - {self.author} (ISBN: {self.isbn}) [{status}]"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            return f"{self.name} borrowed the book: {book.title}"
        return f"{book.title} is currently unavailable."
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            return f"{self.name} returned the book: {book.title}"
        return f"{self.name} did not borrow this book."
    
    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"


class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        return f"Book added: {book.title}"
    
    def register_user(self, user):
        self.users.append(user)
        return f"User registered: {user.name}"
    
    def list_books(self):
        return "\n".join(str(book) for book in self.books)
    
    def list_users(self):
        return "\n".join(str(user) for user in self.users)

def option1():
    Name=input('Enter your name:')
    user1=User(Name,1)
# Example usage
# library = Library()

# book1 = Book("Python Programming", "Guido van Rossum", "123456789")
# book2 = Book("OOP Principles", "Bjarne Stroustrup", "987654321")

# user1 = User("Ali", 1)
# user2 = User("Vali", 2)

# library.add_book(book1)
# library.add_book(book2)
# library.register_user(user1)
# library.register_user(user2)

# print(user1.borrow_book(book1))
# print(user1.return_book(book1))
# print(library.list_books())

show_menu()
while True:
    choice=input('Choice: ')
    if choice == str(1):
        option1()
    elif choice ==str(2):
        option2()
    elif choice == str(3):
         option3()
    elif choice== str(4):
         option4()
    elif choice== str(5):
         option5()
    elif choice.upper() == 'Q':
        print("Goodbye!")
        break
    elif choice.upper() == 'M':
         show_menu()
    else:
        print("Invalid choice, please try again.")