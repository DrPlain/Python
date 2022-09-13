#Pattern one
n = int(input('Enter a whole number: '))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = '')
    print()

#print a number in reverse
n = int(input('Enter an interger to be printed: '))
while n % 10 != 0:
    print(f'{n%10}', end = '')
    n = n // 10
