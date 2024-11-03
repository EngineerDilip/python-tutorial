#Example:

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
#Generators return a generator object. You can iterate over it using a for loop or next() function.
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
#print(next(gen))  # Raises StopIteration

#With for loop
for count in count_up_to(5):
    print(f"count:{count}") 
#Output:
#count:1
#count:2
#count:3
#count:4
#count:5

#Example: Generator for Infinite Sequence
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

gen_even = even_numbers()
even_numbers= [ next(gen_even) for x in range(5)]
print(even_numbers)
#Output: [0, 2, 4, 6, 8]

#Example: Real-World Use Case: Reading Large Files

file_path = 'large_text_file.txt'
with open(file_path,'a') as file:
    file.write("line1\n")
    file.write("line2\n")

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        print("Entered \n")
        for line in file:
            yield line.strip()

for line in read_large_file('large_text_file.txt'):
    print(line)

#Delete the file
import os
os.remove(file_path)


# Example: Coroutine Function grep

"""line = (yield) is a yield expression. When the function is primed (activated by next()), 
it pauses at this line, waiting to receive a value from send(). 
When a line of text is sent using search.send("some text"), 
this line receives that text as line and the function continues execution."""

def grep(pattern):
    print(f"Searching for '{pattern}'")
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep("python")
next(search)     # Initialize generator
search.send("this is python file")
search.send("this is c example")

#Output: this is python file

#Example: Using send() and close()

def echo():
    while True:
        received = (yield)
        print("Received:", received)

gen = echo()
next(gen)         # Initialize generator
gen.send("Hello")  # Received: Hello
gen.send("World")  # Received: World
gen.close()


#Example: Generator Pipelines
""" Generators can be chained together to process data in stages,
 useful for data processing or ETL pipelines."""
#Generator function number() yield 0 yiled 1...yield 4
def numbers():
    for i in range(5):
        yield i

#Generator function squares() yield 0*0, yiled 1*1 ...yield 4*4
def squares(gen):
    for num in gen:
        yield num * num

# Chaining generators
for result in squares(numbers()):
    print(result) # 0 1 4 9 16


#Example: Infinite Generators 

def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#Generate fibonacci series upto 4
gen = infinite_fibonacci()
fibonacci_series = [next(gen) for i in range(4)]
print(fibonacci_series) #[0, 1, 1, 2]
