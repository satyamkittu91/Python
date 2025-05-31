import os
print(os.path.join('usr', 'bin', 'spam'))
print(os.getcwd())

#An absolute path, which always begins with the root folder
#• A relative path, which is relative to the program’s current working directory

#os.makedirs('C:/Programming/Python/Python\Automate_the_boring_stuff_(Book)/Chapter_8/os_test')

#this created a folder named os_test in the current working directory

print(os.path.abspath('os_test')) #this gives the absolute path of the os_test folder
print(os.path.isabs('os_test')) #this checks if the path is absolute or not
print(os.path.relpath('Programming', 'os_test')) #this gives the relative path of the Programming folder from the os_test folder
print(os.path.dirname('os_test')) #this gives the name of the directory of the os_test folder
print(os.path.basename('os_test')) #this gives the name of the os_test folder
print(os.path.split('os_test')) #this gives the name of the directory and the name of the os_test folder as a tuple
print(os.path.splitext('os_test')) #this gives the name of the os_test folder and the extension of the os_test folder as a tuple
print(os.path.getsize('os_test')) #this gives the size of the os_test folder in bytes
print(os.path.exists('os_test')) #this checks if the os_test folder exists or not
print(os.path.isfile('os_test')) #this checks if the os_test folder is a file or not
print(os.path.listdir('os_test')) #this lists the contents of the os_test folder
