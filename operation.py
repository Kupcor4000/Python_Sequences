#lists
rainbow = ['red','orange','yellow','green','blue','indigp','violet','red']
object1 = [1,2,3,4,5]
object2 = [6,7,8,9,10]

#main program
print(rainbow[1:4])
print(rainbow[2:])
print(rainbow[0::2])
print(len(rainbow))
print('red' in rainbow)
print(rainbow.count('red'))
print(rainbow.index('red'))
object3 = object1+object2 + rainbow
print(object3)
object4 = object1 * 4
print(object4)
del object1[0:2]
print(object1)
