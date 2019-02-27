

def main():

    start, end = getrange()
    print('The prime numbers between', start, 'and', end, 'are:')
    
    for number in range(start, end+1):
        valid = prime(number)
        if valid == True:
            print(number)

def getrange():
    start = int(input('What is the first number in your range?'))
    end = int(input('What is the last number in your range?'))
    while end < start:
        end = int(input('Enter an end number greater than the start number:'))
    return start,end

def prime(number):
    
    divisor = 2
    mod = 1
    
    while (mod > 0) and (divisor <= (number - 1)):
        mod = number % divisor
        divisor += 1
    
    if mod == 0:
        return False
    return True

main()
