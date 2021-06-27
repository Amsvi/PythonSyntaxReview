
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

#------------------
# default dic int
from collections import defaultdict
d6 = defaultdict(int)
d6['a']+=2
print(d6['a'])
d6['a']+=3
print(d6['a'])
#---------
account = defaultdict(int)
account['ali']+=20
print(account['ali'])
account['ali']-=15
print(account['ali'])
account['ali']*=1.15
print(account['ali'])
account['ali']/=0.5
print(account['ali'])
#------------------
from collections import defaultdict

rain = defaultdict(list)

rain['aliabad'].append(3)
rain['gorgan'].append(5)
rain['gonbad'].append(5)
rain['day'].append(1)
rain['employee'].append('bairam')

rain['aliabad'].append(13)
rain['gorgan'].append(15)
rain['gonbad'].append(15)
rain['day'].append(2)
rain['employee'].append('amir')

print(rain.keys())
print(rain.values())