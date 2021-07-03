#def , class , exception, sqlite3, array,

class shape:
    def __init__(self):
        print("we r creatin a shape")
    def area(self):
        print("calc area")
s1=shape()
s1.area()
# everything in the world is object, which has attribute and function. for example: human is an object.
# its attribute are H, Weight Color and its function are moving jumping eating...we use class as a blueprint
# for object to reuse this class manay times. after class definiation 13-24 we need initiate it and make an instance24-26.
class rectangle:
    def __init__(self,x,y):
        self.X=x
        self.Y=y
    def area (self):
        A=self.X*self.Y
        return A
    def perimeter(self):
        p=(self.X+self.Y)*2
        return p

rec1=rectangle(3,4) #instance, harche ghable in bud vojod bud inja ijad shod.
A=rec1.area()
p=rec1.perimeter()
print(A,p)