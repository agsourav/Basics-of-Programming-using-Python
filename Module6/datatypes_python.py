"""var1 = 4
var2 = -9.98
var3 = True
print(var1, var2)
print(type(var1), type(var2))

print(type(var3))

print(var1>var2)"""

#list
l = list([3,4,-2,78,'a'])
l1 = [1,2,4,5,6]
print(type(l), type(l1))
#tuple
t = tuple([2,3,5,7,'2f'])
t1 = (2,)
print(type(t), type(t1))
#set
s = set([1,2,3,4,4,5])
print(s)
#dict
d = {'a': 12, 'b': 21, 'tf': 'abc'}
print(d)

#string
str = "hello"
print(type(str))

print(l[1], t[2], d['a'])