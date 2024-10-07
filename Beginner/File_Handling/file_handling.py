
#Open a file and write the data
file = open('example.txt', 'w')
file.write('This is a test.\n')
file.close()

#Open the file and read the content
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("File not found.")
finally:
    if file:
        content = file.read()
        print(content)
        file.close()


# With 
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred {e}")    
# The file is automatically closed here



#Let write some more lines
#Open a file and write the data
file = open('example.txt', 'a') #append the exisiting file
file.writelines(['This is a test-2.\n','This is a test-3.\n'])
file.close()

# read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line,  end='')



# Some os operations 
import os

try:
    if os.path.exists('example.txt') :  #check does file exist
        os.rename('example.txt','new_example.txt')  #throw an error if new_example.txt already exist
except Exception as e:
        print(f"An error occured {e}")
finally:
    os.remove('new_example.txt')   #Dont forget to delete the file