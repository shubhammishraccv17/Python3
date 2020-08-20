
print("open the .py files that will help you understand concepts explained  using comments ")

"""variables
as we know python is dynamically typed language so we dont need to specify variables type at the time of declaration .
variables are container to store a value ""
rules for declaration  of variable"""
#alphabets,numbers and underscore are used to name the variable u can use underscore but varibale cant start and end with underscore 

a=25
print (type(a))
b="25"
print (type(b))
c="alpha"
print (type(c))
d=1.44
print (type(d))
e=1.44444444444444
print(type(e))
f=True
print(type(f))


""" output 
<class 'int'>
<class 'str'>
<class 'str'>
<class 'float'>
<class 'float'>
<class 'bool'>"""



# python is case senstive 

# Multiple assignment of variables 

name,age,sex,nationality="ram",21,"male","india"
print(name,age,sex,nationality)



#swapping variables 
he="i love you "
she="ilove you 2"
he,she = she ,he 
print(she,he)

""""

del he
print(she,he)


output  hkeeper@hkeeper-swan:~/Documents/placement/python$ python3  lesson1.py
open the .py files that will help you understand concepts explained  using comments 
<class 'int'>
<class 'str'>
<class 'str'>
<class 'float'>
<class 'float'>
<class 'bool'>
ram 21 male india
i love you  ilove you 2
Traceback (most recent call last):
  File "lesson1.py", line 50, in <module>
    print(she,he)
NameError: name 'he' is not defined""""

