"""String is a sequence of charecter .there is built in class str for python strings. strings are enclosed inside (' ') single quotes and double quotes(" ") with same result .
"""
str1="i love you "
str2='i love you '
 # how to use quotes inside a string
str3='i love "you"'
print (str3)
str4="i love 'you'"
print (str4)
#slicing of string 
# single charector 
print (str1[5])
print (str1[1:7])
print (str1[1:])
print (str1[ :-1])
print (str1[ :9])
print (str1[-3:])

# string concatination
str5="shubham "
print(str1+str5)


#string replication 

str6=str5*10
print(str6)

# some popular error in strings 

"""str7="10"
print(str7+10)

error from previous line we get is
Traceback (most recent call last):
  File "strings.py", line 32, in <module>
    print(str7+10)
TypeError: can only concatenate str (not "int") to str"""


# string formatters


# how to attach a string with variables 

age =23 
city ="kanpur"
print("my name is " ,str5 ,". my age is ",age, "i am from" ,city )


# f strings
# The letter ‘f’ precedes the string, and the variables are mentioned in curly braces in their places.


print(f"my name is {str5}")



# format method

print ("i love {0}".format(str5))
print ("i love {str8}".format(str8="shubham mishra"))



str9="mishra"



# % operator 

print("i love you %s and %s "%(str5 ,str9))

# %i- integers  
# %f- floating point numbers 
age =22
print("my age is %i " %(age))



#escape sequence
# \n -linefeed 

print("hell\n o")
# \t -tab
print("hell\t o")


"""hell
 o
hell     o"""



# python string function 

# len()-  length of strings

print(len(str1))


#str() -convert other data types in string 

print(str(age))


# lower and upper

print(str1.upper())
print(str1.lower())



#strip()
#It removes whitespaces from the beginning and end of the string.
str11="       robinhood       "
print(str11.strip())



# isdigit

# it gives boolean result that a string is digit or not


str12="000000llllll"
str13="0000000000"
print(str13.isdigit())


#isalpha
#it gives boolean result that a string is alphabet or not



str14="asdfghjkl"
print(str14.isalpha())

#isspace
#it gives boolean result that a string is space or not
a=" "
print(a.isspace())





#startswith  and endswith
print(str5.startswith("sh"))

print(str5.startswith("am"))


str18=str5.find("b")
str19=str5.replace("b","h")
str20=str5.split("b")
str21="*".join(str1)
print(str18,str19,str20,str21,)

