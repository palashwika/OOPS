
class Circle:

    def __init__(self,radius): #self=instance?what is instance
        self.radius=radius
        self.area=3.14159*radius**2
        self.perimeter=2*3.14159*radius

user=int(input("Enter a number for the radius to calculate Area and Perimeter: "))

A=Circle(user)
P=Circle(user)

print("The area is ", A.area)
print("The perimter is ", P.perimeter)

