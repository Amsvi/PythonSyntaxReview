f = [1,2,3,4,5,6,7,0,4]
#the number of List
n= len(f)
print(n)
#--------
s=sum(f)
#mean
mu=s/n
print(mu)
#---------
#empty List/considered as null and false
f1= []
#-----
f1.append(2)
print(f1)
f1.append(3)
print(f1)
f1.append(4)
print(f1)
f1.pop()
print(f1)
f1.pop()
print(f1)
f1.insert(0,1)
print(f1)
f1.insert(3,3)
print(f1)
del f1[0]
print(f1)
f1.remove(3)
print(f1)
f2=[100,200,300,400]
#extend
f1.extend(f2)
print(f1)
print(f1+f2)
#reverse
f1.reverse()
print(f1)
#sort
f1.sort()
print(f1)

#--------
#mutable
Fruit =['Apple','Orange','banana']
Fruit[0]='Orange'
print(Fruit)
#immutable = Error
S = 'Ali'
S[0] = 'a'
print(S)

#shallow copy,
nums = [1,2,3,4,5]
nums1= nums
nums1[0] = 11
print(nums)

#DeepCopy
nums2 = nums.copy()
nums2[0]= 9
print(nums)
print(nums2)