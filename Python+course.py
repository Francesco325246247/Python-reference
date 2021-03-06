
# coding: utf-8

# In[ ]:

#------------Basic Operators------------

#sum
print(2 + 1)

#subtraction
print(3 - 2)

#multiplication
print(2 * 2)

#Power
print(2 ** 2)

#divisions
print(4 / 2.0)
print(int(4 / 2))
print(type(str(4/2)))

#Modulus
print(5 % 2)
print(5 % 1)


# In[ ]:

# ------------ Assignment Operators ------------ 

#equal
=
#increment
+=
#decrement
-=
#multiply
*=
#divide
(=)
#exponent
**=



# In[26]:

#-----------Variables------------

#int
integer_var = 12
print(type(integer_var))

#float
float_var = 2.5
print(type(float_var))

#string
string_var = 'I am a string' "I am a string"
print(type(string_var))

#boolean
a = 2
b = 3
print(type(a==b))
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a>b and b==b)
print(a>b or b==b)


# In[ ]:

#------------Data Type Conversion-------------

#int(x) Cast an int value
#str(x) Cast a string value
#eval(str) Evaluate the string and return an object
#tuple(s) Convert a read-only touples
#list(s) Convert it to a list
#set(s) Convert it to a set
#dict(d) Creates a dictionary. d must be a sequence of (key,value) tuples.


# In[ ]:

#------------Print method------------
x = 'I am a string'
print(x)

age  = 19
sex = "girl"
country = "USA"
name = "Kelly"

print("My name is {} and I am {} years old. I am a {} from {}".format(name,age,sex,country))
print("My name is {name} and I am {age} years old. I am a {sex} from {country}".format(name=name,age=age,sex=sex,country=country))

#string are an array of characters 
string = "I am another string"
string[5]
string[1:5]
string[5:]
string[:5]



# In[ ]:

#------------String formatting: basic methods------------

website = "http://www.MINdwareLaB.org"

print(website.upper())
print(website.lower())
print(website.split("."))
print(website.split("//"))
print(website.split("www"))
print(website.split(".")[1])
print(website.split(".")[2])


# In[ ]:

#------------String formatting: string escape -----------


#\\	Backslash (\)
print("\\")


#\'	Single quote (')
print("\'")


#\"	Double quote (")
print("\"mindwarelab\"")


#\b	ASCII Backspace (BS)
print("Mindwarelab\b")


#\n	ASCII Linefeed (LF)
print("Mindware\nlab")


#\t	ASCII Horizontal Tab (TAB)
print("\tmindwarelab")


# In[ ]:

#------------List vs Touples vs Dictionaries memorandum------------
list1 = [] #this is a list
touples1 = () #this is a touple
disctionaries = {} #this is a dictionary
 


# In[ ]:

#------------List------------
#Similar to the arrays, but it can contain mixed data type

list1 = ["USA", 99, "guns"]
list2 = [44,77,87.7,55]

#len 
print(len(list1))

#type
print(type(list1))

#max
print(max(list2))

#min
print(min(list2))

#sort
list2.sort()
print(list2)

#Adding items to a list
list1.append("chocolate")
print(list1)

#removing items from a list
print("removed: "+ str(list1.pop(1)))
print(list1)

#check an item inside a list
print("x" in ["x",88,"Torino"])



# In[ ]:

#------------Dictionaries------------

dictionary1 = {"key1":"Ferrari","key2":"Mercedes"}
dictionary2 = {"key1":[14,77,54],"key2":"Mercedes"}
dictionary3 = {"key1":{"numbers":[55,43,99]},"key2":"Mercedes"}

#Accessing values inside a nested dictionary
print(dictionary3["key1"]["numbers"][2])

#some extra things you can do with the dictionaries
print(dictionary1.keys())
print(dictionary1.items())
print(dictionary1.values())




# In[ ]:

#------------Set------------
set1 = {1,2,6,7,5,5}
set1.add(9)
set1




# In[ ]:

#------------Touples------------

#touples are read-only 
tup1 = ("moon", "venus", 2017, 2009)
print(tup1)

#Operation on list of touples
num = [(0,1),(1,1),(0,0)]
for a,b in num: print(a)


# In[ ]:

#-----------Logic------------

a = 10
b = 20

if a == b:
    print("Something is wrong here")
elif b == b:
    print("How obvious")
else:
    print("uhm")


# In[ ]:

#------------Repeated actions------------

age_set=[33,56,78,92,11]
for numbers in age_set:
    print("Someone has {} years old".format(numbers))
    print("Increment the age of {} + 1 -> ".format(numbers)+ str(numbers+1)) 

for numbers in list(range(1,10)):
    print(numbers)
    
print(list(range(5)))
    
a = 1
while a < 10:
    print("a is {}".format(a))
    a = a + 1


# In[ ]:

#------------Appending items to a list with a for loop------------

my_list = []
for numbers in range(10):
    my_list.append(numbers **2)
print(my_list)

#List Comprehensions
print([numbers **2 for numbers in range(10)])
print([numbers **2 for numbers in range(10) if numbers % 2 == 0])


# In[20]:

#------------functions------------

def welcome(name = "{error: name not assigned}"):
    global age
    age = 34
    surname = "Black"
    print("hello {}".format(name))

welcome("MindwareLab")
welcome()

def power(numbers, power):
    return numbers **power

output = power(10,2)
power(7,37)

print(output)

print(age)
print(surname)



# In[ ]:

#------------Maps and lambda------------
from functools import reduce
list_of_number = [1,2,3,4,5,6,7,8,9,10]

#maps a function
def power2(num):
    return num **2
print(list(map(power2,list_of_number)))

#labda functions 
print(list(map(lambda n: n**2, list_of_number)))
print(list(map(lambda n: n**2, range(11))))

#Filters
print(list(filter(lambda x: x<=5, list_of_number)))
print(list(filter(lambda x: x%2 == 0, list_of_number)))
print(list(filter(lambda x: x%2 == 1, list_of_number)))

#Reduce
print(reduce((lambda x, y: x*y), [1,2,3,4,5,6,7,8,9,10]))
print(reduce((lambda x, y: x*y), list_of_number))


# In[ ]:

#----------Classes-----------
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+"@mindwarelab.com"
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def increse_salary(self):
        self.pay =  int(self.pay + 10)

#Creating Instance Objects
employee1 = Employee("Frak","Lasagna", 10)

#Accessing Attributes
print(employee1.email.lower())
print(employee1.fullname())
print("Salary before the increase in the salary is equal to {}".format(employee1.pay))

#increase the salary
employee1.increse_salary()
print("Salary after the increase in the salary is equal to {}".format(employee1.pay))

#hiding variable
class Missle_luncher:
    __timer = 0 
    def counter(self):
        self.__timer =+1
        print("{} hours before the next strike.".format(self.__timer))

missle1 = Missle_luncher()
missle1.counter()
#print(missle1.__timer) #AttributeError: 'Missle_luncher' object has no attribute '__timer'

        

        


# In[8]:

# -----------import libraries and Code introspection ------------
import pandas
import numpy


#pandas?
#numpy?
#dir(pandas) #functionality
#pandas.DataFrame?



# In[ ]:

#----------Time handling-----------

import time
import calendar

localtime = time.asctime( time.localtime(time.time()) )
print ("What time is it? {}".format(localtime))
cal = calendar.month(2017, 4)
print(cal)


# In[ ]:

#---------Handling errors ---------

try: #try this code
    pass #some code goes here
except: #if happen this well-know possible exception, please do this
    pass #some code goes here
except: #if happen this well-know possible exception, please do this
    pass #some code goes here
else: #if happens something else that we are not aware of
    pass #some code goes here
finally: #this code will be always execute no matter what
    pass #some code goes here


# In[ ]:

# ----------- Regex ------------
#Regex is something horrible at the first glance, but it is not that bad at all if few focus your attention for few minutes.
#(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])

#<\s*a[^>]*>(.*?)<\s*/\s*a>

# https://regexone.com/


# In[30]:

# ----------- Multithreaded Programming ------------
import _thread
import time


def bomb(name, timer):
    
    while timer > 0:
        #print("{} timer is ticking, {} seconds left\n".format(name, timer))
        timer -=1
        time.sleep(1)
    return print("{} Kabooom!!!\n".format(name))

try:
    _thread.start_new_thread(bomb, ("bomb1",10,))
    _thread.start_new_thread(bomb, ("bomb2",8,))
    _thread.start_new_thread(bomb, ("bomb3",6,))
    _thread.start_new_thread(bomb, ("bomb4",4,))
    _thread.start_new_thread(bomb, ("bomb5",2,))
    _thread.start_new_thread(bomb, ("bomb6",8,))
except:
    print("My God, it is full of stars!")

    
            


# In[ ]:



