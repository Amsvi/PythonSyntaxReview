
#index dar string

#[start:end:step]
t = ['asdasd','adasdasd',2]
#mutable= list /immutable=string
#ordered
#-----------------
s = 'abcjdefghijklmnojpqrst'
print(s.index('k'))
#---------------
p= ['amir','bairam','py']
print(p.index('py'))
#----------------
print(s.find("j"))
print(s.find("j",4))
#---------------
n= s.count("j")
print(n)
#---------
k=0
for i in range(n):
    a=s.find('j',k)
    k=a+1
    print(a)

#-------
#mutable list
Fruit =['Apple','Orange','banana']
Fruit[0]='Orange'
print(Fruit)

#immutable = Error - string
S = 'Ali'
S[0] = 'a'
print(S)
#----
#replace
f1= 'tools.py'
c1 = f1.replace('.py','.csv')
print(c1)
#----
s = 'ALI'
c= s.replace('A','a')
print(c)

#------
num = '12'
print(type(num))
print(num.isdigit())
num1 = int(num)
print(type(num1))

num2 = float(input('Enter a value: '))
print(type(num2))
num3 = float(input('Enter another value: '))
print(num2+num3)

#make a list according to the seprator
s = 'ab,123'
print(s.split(','))
#reverse index/find
p = 'asdasdas'
print(p.rindex('da'))
print(p.rfind("da"))