print('welcome to PYTHON PROJECT2 GROUP OF COMPANY')
name= input('Enter your name:')
from datetime import datetime
c_d = input('Enter appointment date in this format (mm/dd/yyyy):')
c_t = input('Enter time in this format(HH:MM):')

# to search
# find()
def search_strftime(project.py, world):
    with open(project.py, 'r') as file:
          content = file.read()

if c_d:
      print('string exist in a file')
else:
    print('string does not exist in a file')


# write to a text file
file_name = "prj5.txt"
with open("prj5.txt", 'w')as file:
   file.write(f"{name} \n")
   file.write(f"{c_d} \n")
   file.write(f"{c_t} \n")
#read  file
with open('prj5.txt', 'r')as file:
    print("\n contents of the file: ")
    for line in file:
        print(line.strip())
   





