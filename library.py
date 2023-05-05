# class library:
#     books=0
#     def __init__(self,bookname):
#         self.bookname=bookname
#         library.books+=1
#     def showdetails(self):
#         print(f"number {self.books} bookname is {self.bookname}.")
# ob1=library("marvel")   
# ob1.showdetails()
# ob2=library("harrypotter")
# ob2.showdetails()

class library:
    def __init__(self):
        self.noofbooks=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.noofbooks=len(self.books)
    def details(self):
        print(f"The library has {self.noofbooks} BOOKS. The  books are:")
        for book in self.books:
                print(book)
l1=library()
l1.addbook("harrypotter")
l1.addbook("MARVEL")
l1.addbook("ramayan")
l1.details()



