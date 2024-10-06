# if, elif,else (Conditional statement)

# 1. Basic if-else

x = 10
if x > 5:
    print("x is greater than 5")
elif x ==5:
    print("x is equal to 5")
else:
    print("x is smaller than 5")




# 2. For loop (my favrioute)
#Used to iterate over the a sequence (like a list,tuple,dictionary,string, set,range)
#Do not worry we will look into the terminonlogy later

#Iternate over the list
for i in ([1,2,3,4,5]):
    print(i)

#Using range
#range(5) : 0 to 4

for i in range(5):
    print(i)


# 3. While loop : Executes a block of code as long as condition is true

x = 0
while x < 5:
    print(x)
    x+=1


#4. Break statement : Used to exit a loop before it has finished iterating.

for i in range(10):  # 0 to 9
    if i == 5:
        break #Exist the loop when i is 5
    print(i)

#5. Continue statement : skip the current iteration and continues with the next one.

for i in range(10): # 0 to 9
    if i == 5:
     continue       # skip 5
    print(i)

#6. Pass statement:  Used as a placeholder when a statement is required syntactically but
# you dont want to execute any code.

if True:
    pass # Does nothing

for i in range(5):
    pass # Loop does nothing


#7. Else with Loops
# An else clause can be used with loops. The else block is executed after the loop completes normally.

for i in range(5):
    print(i)
else:
    print("Loop finsihed without the break")


x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("while loop finished")


#8. Try-except for Exception handling error and exceptions.

try:
    x = 1/0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception occured")
finally:
    print("This run no matter what")


#9. Match statement ( Python 3.10+)
x =2 

match x:
    case 1:
        print("x is {}".format (x))
    case 2:
        print("x is {}".format (x))
    case _:
         print("x is {}".format(x))

# Output : x is 2


#10. Return statementn (inside function)
#Used to exit a function and optionally return a value.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

#11. Yield statement (in generators)
#Allow a function to return values one at a time and maintain its state between calls.

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

for value in my_generator():
    print(value)

#12. Assert statement
# Used for debugging purposes, to check if a condition is true.

x = 5
assert x > 0, "x should be greater than 0"    #if x> 0 false then it does print


#13 . With statement (Context Management)
#Used to wrap the execution of a block of code within a context manager, often for
# managing resources like files

with open('file.txt','r') as file:
    content = file.read()
    print(content) #Automatically closes the file

