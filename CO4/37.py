class publisher:
    def __init__(self,n):
        self.name=n
    def display(self):
        print("Name of the book is",self.name)
class book(publisher):
    def __init__(self,n,t,a):
        super().__init__(n)
        self.title=t
        self.author=a
    def display(self):
        print("Title of the book is",self.title)
        print("Author of the book is",self.author)
class react(book):
    def __init__(self,n,t,a,p,pgs):
        super().__init__(n,t,a)
        self.price=p
        self.pages=pgs
    def display(self):
        print("Name of the book is:",self.name)
        print("Title of the book is:",self.title)
        print("Author of the book is:",self.author)
        print("Price of the book is :",self.price)
        print("No of pages:",self.pages)
p1=react("Web Development","Advanced Web Development with React","Mehul Mohan",500,204)
p1.display()