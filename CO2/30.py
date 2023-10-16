# Sanu K Joseph
rect=lambda x,y: x*y 
sqr=lambda x: x*x 
tri=lambda x,y: .5*x*y 

print("Area of Rectangle:"+str(rect(int(input("Length of rectangle: ")),int(input("Breadth of rectangle :"))))+"\n") 
print("Area of Square:"+str(sqr(int(input("Side of square: "))))+"\n") 
print("Area of Triangle:"+str(tri(int(input("Base of triangle:")),int(input("Height of triangle: ")))))