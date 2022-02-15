"""
Lets say we are hired by a brick company that sells bricks to people.
The brick company has a single factory that makes certain kind of bricks.
https://capricebaksteen.nl

Now lets say for a given month, an x amount of bricks are produced every week.
The brick factory wants to be able to see how many bricks of a certain type are in stock.
They also want to see how many they are still expected to produce.
In addition to this they want to have a model that shows possible problems with in and output.
During the course of a few lessons we are going to help this brick company achieve this.
We will start each lesson with a bit of theory, and then follow by solving the problems one by one. 

Today we are first going to use functions, loops and global variables in order to manage stock.
Exercise 1a: create some variable to save the amount of stock for the following bricks: "DCR, DCER, WSEMA-B"
Exercise 1b: the first week the amount of produces bricks for WSEMA-B was 1234, the second week 987, the third week 1204, save these in a list.
"""


# * Sometimes we want to save more than a single value at a given time, for this we can use lists, a list is just like an array, lists in python are simple as well
# * You don't have to tell python you are using a list, only by using [] brackets

my_integer = 3
my_list_of_integers = [1, 2, 3, 4]

my_string = "text"
my_list_of_string = ["this", "is", "a", "list"]

my_bool = True
my_list_of_bools = [True, False, True, False]

my_char = 'a'
my_list_of_chars = ['a', 'b', 'c', 'd']

# ? Note that list use [] and , for seperation of the items in a list

# The difference between python and C++ is that where c++ uses brackets {} python usen intendation, so tabs
my_int = 3
if my_int == 3:
    my_int2 = 5
    if my_int2 == 3:
        my_int3 = 20
    elif my_int2 == 5:
        my_int3 = 10
    else:
        my_int4 = 30

test = 5

"""
1: --> check if my_int == 3
1.1 --> if my_int ==3, continue to tab
1.2 --> if my_int == 3 is false, continue to test
"""

#! ERROR WARNING, undefined
my_int2 = my_int2 + 3




# ? Exercise 1a: create some variable to save the amount of stock for the following bricks: "DCR, DCER, WSEMA-B"
# ? 1a.1 what type should this variable be?
# an example of a type is {string}, an example of a variable = my_string, an example of a value = 5
# ! Answer of sam: Integer, this is correct

# ? 1a.2 implement these variables
dcr_old = 0
dcer_old = 0
wsema_b_old = 0

# *  more easy implementation (as mentioned by sam)
dcr2, dcer2, wsema_b2 = 0, 0, 0

# * even more easy implementation
dcr, dcer, wsema_b = 0

# ? Exercise 1b: the first week the amount of produces bricks for WSEMA-B was 1234, the second week 987, the third week 1204, save these in a list.
# ! answer of sam
wsema_b_production = [1234, 987, 1204] 

# ? Exercise 1c: create a list of strings contain the texts: week 1, week 2, week 3
weeks = ["week 1", "week 2", "week 3"]

# ? Exercise 1d: first print the week list, then print the production value list
print(weeks) 
print(wsema_b_production)

# ? Exercise 1e:
# ? Lets say the boss of the brick factory wants to know how many bricks to expect next week, can we give him an indiciation of this?
# ? Hint, calculate the average
average = (1234 + 987 + 1204) / 3
print(average)

# ? Exercise 1f, create a stock that is the combination of all the production in a list. 

# * Lesson
# * we can iterate over lists using for loops (i know they sound scary)
# * for loops in python are absolutely amazing, they are much more easy to use then c++ loops (hope that makes it less scary)

# * lets say we want to do something ten times
# * this will run ten times and print 0 to 9 (SO NOT 10), due to counting from 0
for i in range(10):
    print(i)
    
for i in weeks:
    print(i)

#output of above code:
# week 1
# week 2
# week 3

#lets say we want 0 + 1 + 2 + 3 + 4 + 5 + 6 +  7 + 8 + 9
output = 0
for number in range(10):
    output = output + number
print(output)

dcer_production = [1234, 987, 1204, 2343, 23432, 564, 7556, 756, 1024, 422, 458, 420, 888, 1242, 5325, 235] 

# ? Exercise 1g, what is the total amount that is produced, save it to integer stock_dcer
dcer_stock = 0 
for day_production in dcer_production:
    dcer_stock = dcer_stock + day_production
    print(dcer_stock)
    
"""
1234
2221
3425
5768
29200
29764
37320
38076
39100
39522
39980
40400
41288
42530
47855
48090
"""

dcer_weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
dcer_production = [1234, 987, 1204, 2343, 23432, 564, 7556, 756, 1024, 422, 458, 420, 888, 1242, 5325, 235] 
dcer_orders = [0, 0, 0, 0, 3152, 0, 0, 4542, 0, 0, 14245, 0, 0, 0, 142, 0]

#print(len(dcer_weeks))
#print(len(dcer_production))
#print(len(dcer_orders))
"""
16
16
16
"""

stock = 0
for i in range(len(dcer_weeks)):
    stock = stock + dcer_production[i]
    stock = stock - dcer_orders[i]
    print("week " + str(dcer_weeks[i]) + ", the production was: " + str(dcer_production[i]) + " the orders were: " + str(dcer_orders[i]), " the current stock is: " + str(stock))
    
"""
week 1, the production was: 1234 the orders were: 0  the current stock is: 1234
week 2, the production was: 987 the orders were: 0  the current stock is: 2221
week 3, the production was: 1204 the orders were: 0  the current stock is: 3425
week 4, the production was: 2343 the orders were: 0  the current stock is: 5768
week 5, the production was: 23432 the orders were: 3152  the current stock is: 26048
week 6, the production was: 564 the orders were: 0  the current stock is: 26612
week 7, the production was: 7556 the orders were: 0  the current stock is: 34168
week 8, the production was: 756 the orders were: 4542  the current stock is: 30382
week 9, the production was: 1024 the orders were: 0  the current stock is: 31406
week 10, the production was: 422 the orders were: 0  the current stock is: 31828
week 11, the production was: 458 the orders were: 14245  the current stock is: 18041
week 12, the production was: 420 the orders were: 0  the current stock is: 18461
week 13, the production was: 888 the orders were: 0  the current stock is: 19349
week 14, the production was: 1242 the orders were: 0  the current stock is: 20591
week 15, the production was: 5325 the orders were: 142  the current stock is: 25774
week 16, the production was: 235 the orders were: 0  the current stock is: 26009
"""

# ? Now calculate the average of the production again, into an int with name dcer_average

dcer_weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
dcer_production = [1234, 987, 1204, 2343, 23432, 564, 7556, 756, 1024, 422, 458, 420, 888, 1242, 5325, 235] 
dcer_orders = [0, 0, 0, 0, 3152, 0, 0, 4542, 0, 0, 14245, 0, 0, 0, 142, 0]

total_production = 0
for single_production in dcer_production: 
    total_production = total_production + single_production
    
average = total_production / 16
current_stock = 26009

# ? We know now that there is a big order of 42524 stones in week 24 can the company fullfill this order?
seven_weeks =  average * 7
stock_in_seven_weeks = current_stock + seven_weeks
print(stock_in_seven_weeks)

if (stock_in_seven_weeks < 42524):
    print("You will probably not be able to get the order done in time.")
else:
    print("You will probably get the order done in time, expected surplus is: " + str(stock_in_seven_weeks - 42524))
    

# ? Lets say that there is an order in week 44 of the year for 106000 stones, will they make the order?
# ? If they will make the order, show the expected surplus, if they will not make the order, show how many stones they fall short.

# * hint: use the current stock, the amount of weeks left and the average, to calculate the stock at the given time

dcer_weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
dcer_production = [1234, 987, 1204, 2343, 23432, 564, 7556, 756, 1024, 422, 458, 420, 888, 1242, 5325, 235] 
dcer_orders = [0, 0, 0, 0, 3152, 0, 0, 4542, 0, 0, 14245, 0, 0, 0, 142, 0]

total_production = 0
for single_production in dcer_production: 
    total_production = total_production + single_production

average = total_production / 16
current_stock = 26009

stock_produced_later = average * 28 
stock_in_weeks_to_go = current_stock + stock_produced_later

if (stock_in_weeks_to_go < 112000):
    print("You will probably not be able to get the order done in time." + str(112000 - stock_in_weeks_to_go ))
else:
    print("You will probably get the order done in time, expected surplus is: " + str(stock_in_weeks_to_go - 112000))

# FIRST: some more simple exercises and redoing
# THEN: some cool linear regression (super easy!)

# VARIABLES
# integer, string, double, boolean

# ARITHMETHICS
thirty = 30
fourty = 40

#inside a variable named seventy, add thirthy and fourty together

seventy = thirty + fourty

#inside a variable named output, do 7 times thirty + 8 times fourty, then substract 15

output = (7 * 30 + 8 * 40 - 15) 

# STRINGS
# make a string with as text "hello world", call it however you like

string = "Hello World"

# Add the text " 2022" to the above string using arithmetics

text = string + " 2022"

# replace the Hello with goodbye in the above string

replacement = text.replace("Hello", "Goodbye")

# showcase this to the user

print (replacement)

# LISTS AND LOOPS 

# create a list containing three names of your choice

names = ["Sam1", "Sam2", "Sam3"]

# print the second element of the list
element = names[1]
print (element)

for name in names:
    print(name + " works")
    
elem_one = names[0]
print(elem_one)
elem_two = names[1]
print(elem_two)
elem_three = names[2]
print(elem_three)

numbers = [123, 235, 3435, 3453, 705, 755, 744, 345, 785]

# Now the company wants to know how much they earned in total
# use a for loop to calculate the total earnings of the company

output = 0
for profit in numbers:
    output = output + profit
print(output )

babynames = ["chleo", "patrick", "eric", "pieter"]

for name in babynames:
    print(name)
    
allnums = [-3, -2, -1, 0, 1, 2, 3]

for thesenames in allnums: 
    print(thesenames)

bools = [True, False, False, False, False, True, True, False, True, True, True]

# print every element of this list

# for loop part 1
# find the first name
# Sam1 found
# print Sam1
# Sam1 found is there more?
# Found sam2 
# print sam2

names
# Coding from documentation

# Linear regression