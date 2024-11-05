###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard1 # your own defined module

# Reads employee's data from keyboard
first_name = keyboard1.input_string('Enter name: ')
last_name = keyboard1.input_string("Enter last name: ")
age = keyboard1.input_integer("Enter age: ")
salary = keyboard1.input_real("Enter salary: ")
is_salary_hidden = keyboard1.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name:', first_name," ",last_name)
print(f"Age: ",{age})
#print(...)
if is_salary_hidden == False:
    print(f'Salary: ',{salary})