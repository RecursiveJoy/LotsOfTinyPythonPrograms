number = int(input("Enter a number to see if it is prime "))
divisor = 2
mod = 1

while (mod > 0) and (divisor <= (number - 1)):
    mod = number % divisor
    divisor += 1

if mod == 0:
    print(number, "is not prime.")
else:
    print(number, "is prime.")
