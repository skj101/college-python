# Sanu K Joseph
class rectangle:
    def __init__(self):
        self.__length=int(input("Enter length:"))
        self.__breadth=int(input("Enter breadth:"))
    def __lt__(self,ob2):
        area1=self.__length * self.__breadth
        area2=ob2.__length *ob2.__breadth
        print("the area1:",area1)
        print("the area2:",area2)
        return (area1<area2)
print("Enter Rectangle 1 info :")
rct1=rectangle()
print("Enter Rectangle 2 info :")
rct2=rectangle()
print("Rectangle 1 is smaller")if rct1<rct2 else print("Rectangle 2 is smaller")