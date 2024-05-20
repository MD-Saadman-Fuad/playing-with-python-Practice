#String method
print('String method')
name='Trying to Code'
name1='little'
print(name)

print(name.find("t")) #if -1 then its not in the string
print(name1.find("a"))

print(name1.capitalize())
print(name1.upper())
print(name.lower())
print(name.isdigit()) #digit or not
print(name.isalpha()) # check if only letters
print(name.count('t'))
print(name.replace('o', 'a'))
print(name*3)

#type casting
print('Type Casting')

x = 1
y = 2.0
z = '3'
print(x, y, z)
print(int(y))
print(int(z))

#Taking user input

print('Taking user input')

#name = input('What is your name? ')
print(name)

#Math Functions
print('Math Functions')

import math

pi = 3.14
x=1
y=2
z=3

print(round(pi)) #Rounds to the closest whole number
print(math.ceil(pi)) # rounds up to the next whole number
print(math.floor(pi)) #round down
print(abs(pi)) #how far a number is away from 0
print(pow(pi, 2)) #Power function pi^2
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))

#String slicing
print('String slicing')
#Indexing[start:Stop:step]
name='Bro Code'

first_name=name[0:3]
last_name = name[4:8]
funky_name=name[0:8:2]
reverse_name=name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reverse_name)

#Slice

website = 'http://google.com'
website1 = 'http://yahoo.com'
slice = slice(7, -4, 1)

print(website[slice])
print(website1[slice])

#loop control statements
print('loop control statements')
# break = used to terminate the loop entirely
# continue = skip to next iteration
# pass = does nothing, acts like a placeholder

while True:
    #name = input('Enter Name: ')
    if name !='':
        break
phone_number = '123-456-789-0'''
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

#lists
print('Lists')

food= ['pizza', 'hotdog', 'biriyani']
food[0]= 'sushi'

print(food[0])

for i in food:
    print(i)

food.append('cream')
food.remove('sushi')
food.pop() #will remove last element
food.insert(0, 'cake')
food.sort()
food.clear() #clears lists

#2D lists
print('2D Lists')

drinks =['coffee', 'soda', 'coke']
dinner=['pizza', 'ham', 'biriyani']
dessert=['cake', 'ice', 'cream']

food = [drinks, dinner, dessert]
print(food)
print(food[0])
print(food[0][0])

#Tuple ordered and unchangeable
print('tuples')

student= ('bro', 21, 'male')
print(student.count('bro')) #same element in the tuple count
print(student.index('male')) # element present in index count

for x in student:
    print(x)

if 'bro' in student:
    print('Its there')

#set unordered , unindexed, no duplicates
print('Set')

utensils= {'fork', 'spoon', 'knife'}
dishes ={'bowl', 'napkin', 'cup', 'knife'}

for i in utensils:
    print(i) # print will always be in different order , duplicates will be cancelled
             # and is easy to use in case we want to find if an element is there in the set or thing

#utensils.add('napkin')
#utensils.remove('fork')
#utensils.clear()
#utensils.update(dishes) #dishes added to utensils
#dinner_table = utensils.union(dishes) #adds both set
print(dishes.difference(utensils)) # not in both
print(utensils.intersection(dishes)) # common in both

#Dictionary
print('Dictionary') # changeable, unordered and unique key:value pairs
                    # fast because this uses hashing which helps us find the element faster
capitals = {"USA" : "Washington DC",
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'}) # updating existing element
capitals.pop('China') #Works as a remove function
#capitals.clear()
#print(capitals['USA'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

#Index Operator
print('index operator')

name = 'bro Code'
if (name[0].islower()):
    name = name.capitalize()
print(name)
first_name=name[0:3].upper()
last_name = name[4:].lower()
print(first_name)
print(last_name)

#functions
print('---Review Functions---')
#return statements
print('----Review Return----')
# Keyword  Arguments
print('--Keyword Argument---')
def hello(first, middle, last):
    print('Hello ' + first+' ' + middle + ' '+ last)

hello('Bro', 'Code', 'Dude')

#Nested Function Calls
print('---Review Nested Function Calls---')
#print(round(abs(float(input('Enter a whole positive number: ')))))

#Variable Scope
print("---Variable Scope---")
# Python follows the following sequence
#1. L = Local
#2. E = Enclosing
#3. G = Global
#4. b = Built-in
name = 'Bro' # global scope available inside outide region (functions)

def display_name():
    name ='Code' # Local scope only available inside the function or region
    print(name)
display_name()
print(name)

#*args perameter that will pack all arguments into a tuple
#useful so that a functons can accept a varying amount of arguments
print('---*args---')

def add(num1, num2):
    sum = num1 + num2
    return sum
print(add(1, 2)) # this is the normal way of sum but we can only add 2

#using *args
def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(add(1,2,3,3,4,56,67,7)) #now we can ad multiple stuff using args
#as we have passed a tuple we cant change the values
#to do that we have to change the tuple to a list
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum+=i
    return sum
print(add(1,2,3,3,4,56,67,7)) # the important thing is the * not args

#**kwargs
print('---**kwargs---')
#packs all arguments into a dictionary
# can accept varying amount of keyword arguments

def hello(first, last):
    print('Hello'+' ' +first +' '+last)
hello(first="Bro", last="Code")

#to apply **kwargs
def hello(**kwargs):
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')
hello(title='Mr.', first="Bro", middle='Dude', last="Code")