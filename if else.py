#dic ,loop, file ,def , class , exception, sqlite3, array,

age = float(input("enter your age: "))

if age>12:
    print('you can go to cinema')
else:
    print('you can not go to cinema')
#---------------
age = float(input("enter your age: "))
if age>12:
    print(f'you can go to cinema since your age is {age}')
else:
    print('you can not go to cinema')
#--------------------
if age<=2:
    print(f'you are infant {age}')
elif age>2 and age<=12:
    print('you are child')
elif age>12 and age<=20:
    print('you are teenager')
elif age>20:
    print('you are old')
else:
    print('you can not in the range')

#-------------------------
#reclassify on group ( discretize ), making countiouns to catogories.
age = float(input("enter your age: "))

if age<=2:
    print(f'you are infant {age}')
elif age<=12:
    print('you are child')
elif age<=20:
    print('you are teenager')
elif age>20:
    print('you are old')
else:
    print('you can not in the range')

#----------------
#nested if
age = input("enter your age: ")

if age.isdigit():
    age = int(age)
    if age <= 2:
        print(f'you are infant {age}')
    elif age <= 12:
        print('you are child')
    elif age <= 20:
        print('you are teenager')
    elif age > 20:
        print('you are old')
    else:
        print('you can not in the range')
else:
    print('enter a number')

#zero is false, other number are true, NONE

a = 0
if a:
    print('a is not zero')
else:
    print('a is zero')

#None
kl=[]
if kl:
    print('kl is not empty')
else:
    print('kl is empty')
#lenth is zero,
s=''
if s:
    print('s is false')
else:
    print('s is true')

#simplify
number = float(input("pls enter number: "))
#----if number%2==0:
if number%2:
    print('is an odd number')
else:
    print('is an even number')
