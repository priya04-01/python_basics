# file can be opened using read or write mode
file=open('test.py')
[Errno 2] No such file or directory

file=open('test.py','w')
creates a file if not available


# code for file handling
file=open('youtube.txt','w')

try:
    file.write('Hello World')
finally:
    file.close()

# file handling using with
with open('youtube.txt','w')as file:
file.write('Hello World')