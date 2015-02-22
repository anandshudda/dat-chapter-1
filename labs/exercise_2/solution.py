
# Function that returns the nth term in the Fibonacci sequence 
def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)

# List container to hold all the even values under 4 million 
x = []

# Counter for the while loop
n = 0

# Loop to get the require fib values
while (fib(n) < 4000000):
    value = fib(n)
    n = n + 1
    if (value % 2 == 0):
        x.append(value)

# Summation of all the values to get the answer     
sum(x)