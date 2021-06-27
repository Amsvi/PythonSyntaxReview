
#dictionary, bar asas key farakhoni mishe.
#way1
d= {'Ali': 32,'zahra':43,'hasan':42 }
print(d['Ali'],d['hasan'],d)
d['ali'] = 36
d['Ali'] = 35
del d["Ali"]
print(d)
#way2
d1= dict(one=1,two=2,three=3)
print(d1)
#way3
d3= dict([('one',1),('two',2)])
print(d3)
#way4
d4 =dict(zip(['one','two'],[1,2]))
print(d4)
#way5  ( defult dict )


#
# we cannot use dict and list as primary keys. they are mutable.
# we can use tuple and string instead since they are immutable

#1-dict and list
colors = {'blue':[255,0,0],
          'red':[0,0,255],
          'green':[0,255,0],
          'white':[255,255,255]
          }
b= colors['blue']
print(b)

#1-dict and tuple
colors = {(255,0,0):'blue',
          (0,0,255):'red',
          (0,255,0):'green',
          (255,255,255):'white'
          }
b= colors[(255,0,0)]
print(b)

#we cannot use list as key in dict since list is mutable.
nums = {[1,2]:'one two'}

#way5  ( default dict )
from collections import defaultdict
# we use defaultdict function by one argument as list
d5= defaultdict(list)
d5['nums'].append(3)
print(d5.keys())
print(d5.values())
print(d5['nums'])