###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   r = (x+y)/2.0
   return r

# takes two numbers from keyboard
n1 = int(input("First number: "))
n2 = int(input("Second sumber: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')