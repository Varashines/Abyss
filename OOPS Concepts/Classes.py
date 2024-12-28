

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def details(self, name, age):
    #     self.name = name
    #     self.age = age

    def printdetails(self):
        print(self.name , self.age)

person1 = person('Vara',25)
#person1.details('Vara',25)
person1.printdetails()

person2 = person('Teju',26)
person2.printdetails()

class Library:
    def __init__(self, ListofBooks):
        self.availableBooks = ListofBooks

    def displayAvailableBooks(self):
        print("Here is a list of avialable Books")
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available")

    def addBook(self,returnedBook):
        print("You have now returned the book")
        self.availableBooks.append(returnedBook)

class Customer:
    def requestBook(self):
        print("Enter the name of the book you would like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you would like to return")
        self.book = input()
        return self.book

library = Library(['Mocking Bird','Moby Dick'])
customer = Customer()
while True:
    print("Enter 1 to diaplay the avilable books")
    print("Enter 2 to lend a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    i = int(input())

    if i == 1:
        library.displayAvailableBooks()

    elif i == 2:
        requestbook = customer.requestBook()
        library.lendBook(requestbook)
    elif i == 3:
        returnbook = customer.returnBook()
        library.addBook(returnbook)
    elif i == 4:
        quit()
