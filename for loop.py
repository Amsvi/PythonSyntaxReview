#loop, file ,def , class , exception, sqlite3, array,

d= {'Ali': 32,'zahra':43,'hasan':42 }
colors = ['red','blue','yellow','white']




#---- 
for color in colors:
    print(color)
# -range is a function can make list ( generator )
nums = range(100, 48, -2)

print(nums)

for i in nums:
    print(i)
nums = range(3,10)
print(type(nums))
print(list(nums))
j=[]
k=0
for i in nums:
    k+=i
    j.append([i,k]) #accumaulation
    print(i,k)
print(j)

#------------------
#-range is a function can make list ( generator )

from collections import defaultdict
d1 = defaultdict(list)
d2 = defaultdict(int)
nums = range(1,10)
k=0
for i in nums:
    d1["num"].append(i)
    d2["s"]+=i
    k+=i
    d1["acc"].append(k)
print(d1)
print(d1["num"])
print(d1.keys())
print(d2["s"])

#------------------accumulation
from collections import defaultdict
d1 = defaultdict(list)
d2 = defaultdict(int)
nums = range(1,10)
k=0
for i in nums:
    d1["num"].append(i)
    d2["s"]+=i
    k+=i
    d1["acc"].append(k)
for i,j in zip(d1["num"],d1["acc"]):
    print(i,j)

#---------
from collections import defaultdict
d1 = defaultdict(list)
d2 = defaultdict(int)
nums = range(1,10)
#k=0
d2["m"]+=1
for i in nums:
    d1["num"].append(i)
    d2["s"]+=i
    #k+=i
    d1["acc"].append(d2["s"])
    d2["m"]*=i
    d1["product"].append(d2["m"])
for i,j,k in zip(d1["num"],d1["acc"],d1["product"]):
    print(i,j,k)
# -------- for loop in string
st = 'askjhgtfderty'

for i in range(len(st)):
    print(st[i])

# for loop in string
st = 'askjhgtfderty'
for i in range(len(st)):
    print(st[i])

#----- for loop in dic
d= {'Ali': 32,'zahra':43,'hasan':42 }
for key in d:
    print(key,d[key])
#----------- Normal list --------
k=[]
nums = range(1,10)
for i in nums:
    k.append(i**2)
print(k)
#----------- list comprehension --------
k2=[i**2 for i in nums]
print(k2)
#------------
k3=[i**2 for i in nums if not i%3]
print(k3)
#------------
answer = input("pls write yes or no: ")

while  "YES" == answer.upper():
    print('you said ')
    answer = input("pls write yes or no: ")
