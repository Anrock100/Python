def fibonacci_series(n):
  if n<0:
    print("Incorrect input")
  elif n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci_series(n-1) + fibonacci_series(n-2)

# Driver code to test the function
n = int(input("Enter the number of terms in the series: "))
print("Fibonacci series:")
for i in range(n):
  print(fibonacci_series(i))
