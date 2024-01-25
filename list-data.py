#print the length of the string

var="hello world"
print(len(var))

#print the length of the string

count=len(var)
print(count)

#print specific character
print(var[0])
print(var[7],var[9])
print(var[7:11])
#here the 11 will be not consider and print till 10 index starting from 7

#reverse indexing
print(var[-1])
print(var[-2])
print(var[-5])
#how to declare a list
num=[]
num=[1,2,3,4,5]
print(num)
#to print the specific index value
print(num[4])
#to add element to the existing list
num.append(35)
print(num)
num.append(76,)
print(num)
#how to remove the last element of a list
num.pop()
print(num)
num.pop(1)
print(num)
#how to replace the element 
num[1]=2024
print(num)
var=["hi","hello","hey"]
num.extend(var)
print(num)
