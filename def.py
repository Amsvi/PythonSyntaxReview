#def , class , exception, sqlite3, array,
#--------simple--------
def add2 (x):
    y=x+2
    return y
z2=add2(3)
#------------obligatory --------
def sum2 (x,y):
    z=x*y
    return z
z1=sum2(3,4)
print(z1)
#-------------------------
def circle(r,pi=3.14):
    p=2*pi*r
    area=pi*r**2
    return p,area
z3= circle(2)
print(z3)
