#def , class , exception, sqlite3, array,

#-------------we make a varibale named args which is tuple---------
def average (*args):
    return sum(args)/len(args)
nums = range(2,40)
y=average(*[1,2,3,4])
print(y)
#------------- kwargs = dict-----args = tuple--------
def area (*args,**kwargs):
    if len(args)==1:
        print("shape is circle")
        #- print(args) - (3,) baray inke virgolo(,) dar biarim az tuple ozv avalo mizanim [0]
        r=args[0]
        pi=kwargs['pi']
        return pi*r**2
    elif len(args)==2:
        print("shape is rectangle")
        a,b=args
        return a*b
    elif len(args)==3:
        print("shape is triangle")
        a,b,c=args
        s=sum(args)/2
        ar=(s*(s-a)*(s-b)*(s-c))**0.5
        return ar

y=area(3,pi=3.14)
print(y)
#------------------ Lambada ------------------
add2=lambda x:x+2

def add2(x):
    return x+2
#---------
add3 = lambda x,y:x+y
z=add3(2,3)
#-------------------------------------
