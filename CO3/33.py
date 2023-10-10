class rect():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.breadth+self.length)
    def compare(self,compare):
        if self.area() == compare.area(): 
          print("Areas are equal") 
        elif self.area() > compare.area(): 
          print("Area-1 is greatest") 
        else: 
          print("Area-2 is greatest") 

r1=int(input("\nLength of first rectangle: "))
r2=int(input("Breadth of first rectangle: "))

r3=int(input("\nLength of second rectangle: "))
r4=int(input("Breadth of second rectangle: "))

obj1=rect(r1,r2)
obj2=rect(r3,r4)

print ("\nArea of rectangle-1:",obj1.area())
print ("Perimeter of rectangle-1:",obj1.perimeter(),"\n")
print ("Area of rectangle-2:",obj2.area())
print ("Perimeter of rectangle-2:",obj2.perimeter(),"\n")

obj1.compare(obj2)