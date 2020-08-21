# python does'nt have arrays.
"""it comes with built in class called list
"""
#declaration of list 
list1=["ram","ghanshyam","dubey"]
age=list()


#how to access single element in a list
#listname[indexno]
var=list1[2]


days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(days[0:4])

print(days[-2])


#python list are mutable you can modify you can modify the complete list or even single element in the list 



#to delete a list y
del list1


#python list operation 

#multiplication operator
numbers=[1]*20




#membership operator
print(1 in numbers) 
print(2 in numbers) 
print(1 not in numbers) 
print(2 not in numbers) 
"""#multidimensional lists 








companies=[["neurogen","neuslo","omnito"],["cognito","sunat","mortion"]]
print(companies[[0][1][1]])"""


#concatenation of list
print(days+numbers)



#python list comprehension


list3=[x**2+x+7 for x in range(1,21)]


print(list3)

list4=[x**7+2*x**6+3*x**4+4*x**2+x+19 for x in range(1,100)]
print(list4)





# some built in function in list 


#len()
print(len(list4))

#max()
print(max(list4))


#min()

print(min(list4))


#sum

print(sum(list4))

#sorted
print(sorted(list4))


#list
"""it convert data types into list """
print(list("shubham"))


#built in methods
#append
for x in range(1,17):
    age.append(x)
print(age)

#insert 

age.insert(-1,"invalid")
print (age)