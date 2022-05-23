num = int(input('Please enter the size of Fibonacci list greater than 1: '))

f = 0                                         
sum = 1
if num <= 0:
    print("The fibonacci series is: ", f)
else:
    print(f, sum, end=" ")
    for x in range(2, num):
        next = f + sum
        print(next, end=" ")
        f = sum
        sum = next
