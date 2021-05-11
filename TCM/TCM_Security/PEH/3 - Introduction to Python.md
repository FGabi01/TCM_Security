# Introduction to Python
## Strings
~~~bash
#Print string  
print("Hello world")  
  
print("""This string runs  
multiple lines!""")  
print("This string is" + " awesome") #we can also concatenate
~~~

---

## Math
~~~bash
#Math  
print(50 + 50) # add -> 100  
print(50 - 50) # subtract -> 0  
print(50 \* 50) #multiply -> 2500  
print(50 / 50) #divide -> 1.0  
print(50 + 50 - 50 \* 50 / 50) #PEMDAS -> 50.0  
print(50 \*\* 2) #exponents -> 2500  
print(50 % 6) #modulo -> 2  
print(50 // 6) #no leftover -> 8
~~~

---
## Variables & Methods
~~~bash
#Variables and Methods

quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #give back the length of the string

name = "Gabor" #string
age = 18 #int int(18)
gpa = 4.85 # float float(4.85)

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

#Variables
string - name = “text”
int - name = number
float - name = number.number
bool - name = True/False
~~~

---

## Functions
~~~bash
#Functions

def who_am_i():
	name = "Gabor"
	age = 18
	print("My name is " + name + " and I am " + str(age) + " years old.")

#adding parameters
def add_one_hundred(num):
	print(num+100)

#multiple parameters
def add(x,y):
	print(x + y)

def multiply(x,y):
	return x * y
	
def square_root(x):
	print(int(x ** .5))

def new_line():
	print('\n')
new_line()
~~~

---

## Boolean Expressions
~~~bash
#Boolean expression (True or False)

bool1 = True
bool2 = 3*3 == 9 #-> True
bool3 = False 
bool4 = 3*3 != 9 #-> False
print(type(bool1)) #-> <class 'bool'>
~~~

---

## Relational and Boolean Operators
~~~bash
#Relational and Boolean Operators  
  
greater_than = 7 > 5 #True  
less_than = 5 < 7 #True  
greater_than_equal_to = 7 >= 7 #True  
less_than_equal_to = 7 <= 7 #True  
  
test_and = (7 > 5) and (5 < 7) #True  
test_and2 = (7 > 5) and (5 > 7) #False  
test_or = (7 > 5) or (5 < 7) #True  
test_or2 = (7 > 5) or (5 < 7) #True  
  
test_not = not True #False
~~~

---

## Conditional Statements
~~~bash
def alcohol(age,money):
	if (age >= 18) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 18) and (money < 5):
		return "Come back with more money."
	elif (age < 18) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young"
~~~

---

## Lists
~~~bash
#Lists - Have brackets []

movies = ["When Marry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
print(len(movies)) #returns the number of items in the list
print(movies[0]) #returns the first item of the list
print(movies[1:3]) #returns from what we gave to the stop example [0,1,2,3,4,5] 1:3 -> 1 and 2
print(movies[1:]) #returns from the second item
print(movies[:1]) #returns the first item
print(movies[-1]) #return last item

print(len(movies)) #returns the length of the list 
movies.append("JAWS") #add a new item to the end of the list
movies.pop() #removes the last item
movies.pop(0) #removes the first item
~~~

---

## Set
~~~bash
# Sets - have curly brackets {}
# After creation, we cannot remove but add items

thisset = {"apple", "banana", cherry}

# Remove item
thisset.discard("banana")
# Or
thisset.remove("banana")
~~~

---

## Tuples
~~~bash
#Tuples have parentheses, ()
  
grades = ("a", "b", "c", "d", "f")  
print(grades[1])
~~~

---

## Dictionaries
~~~bash
#Dictionaries - key/value pairs {}  
  
drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} #drink is key, price is value  
print(drinks)  
employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teedy"], "HR": ["Jimmy Jr.", "Mort"]}  
print(employees)  
employees['Legal'] = ["Mr. Frond"] #add a new key/value pair  
print(employees)  
employees.update({'Sales'}: ["Andie", "Ollie"]) #add a new key/value pair  
print(employees)  
  
drinks['White Russian'] = 8  
print(drinks)  
  
print(drinks.get("White Russian"))
~~~
---

## Looping
~~~bash
#Looping for, while  
  
#For loops - start to finish of an iterate  
vegetables = ["tomato", "cucumber", "cabbage"]  
for x in vegetables:  
print(x)  
  
# Print numbers from 0 to x-1
for i in range(0, x):
   print(i)
   
# Print every 2. number from 0 to x-1
for i in range(0, x, 2):
   print(i)
   

#While loops - Execute as long as true  
i = 1  
while i < 10:  
print(i)  
i += 1
~~~

---


## Advanced Strings
~~~bash
#Advance strings  
  
my_name = "Gabor"  
print(my_name[0])  
print(my_name[-1])  
  
sentence = "This is a sentence."  
print(sentence[:4]) #print out the first word  
print(sentence.split())  
  
sentence_split = sentence.split()  
sentence_join = ' '.join(sentence\_split)  
print(sentence_join)  
quote = "He said \"Give me all your money!\"" #->He said "Give me all your money!"  
print(quote)  
  
too_much_space = " hello "  
print(too_much_space.strip) -> hello  
print("A" in "Apple") #-> True  
print("a" in "Apple") #-> False  
  
letter = "A"  
word = "Apple"  
print(letter.lower() in word.lower()) # Improved -> True  
  
movie = "The Hangover"  
print("My favourite movie is {}, and my favourite fruit is {}".format(movie,word)) -> My favourite movie is The Hangover, and my favourite fruit is Apple.

age = 28
print(f"You are {age} yours old") # f is for format string, you can pass variables to the string being printed out

# You might will see that you cannot print a string, because it requires string, using str(data) you can convert it to string
number = 21
print(f"{str(number)}") # IF REQIURED
~~~

---

## File read/write
~~~bash
# Open file
f = open("filename.extension", "r") # Open file in read mode

# Iterating through the file
for i in f.readlines():
   print(i)

# Open a file and save it's content to a list

data=[]
f = open("filename")

data = [line.rstrip('\n') for line in file]

# Appending to file(if file is not created, creates one)
f = open("filename.extension", "a") # Open file in append mode
f.write("New line")

# Write to a file(if file exist, it overwrites any existing content)
f = open("filename.extension", "w") # Open a file in write mode
f.write("Line")

# Create a file
f = open("filename.extension", "x")

# Closing file
f.close()

~~~
---

## Important Modules
~~~bash
import sys #system function and parameters  
from datetime import datetime as dt #import with alias  
  
print(dt.now())
~~~

---

## Socket and Port Scanner

Used for connecting to a open port of an IP address  
Connect two nodes together

 s.py
~~~bash
#!/bin/python3  
  
import socket  
  
HOST = '127.0.0.1'  
PORT = 8888  
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is like IPv4, and SOCK_STREAM is like the port  
s.connect((HOST, PORT))
~~~

 scanner.py
~~~bash
#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip address")
#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started " + str(dt.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
~~~

---