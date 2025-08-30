def collatz(number):
    if number % 2 == 0:
        print(number // 2 , end=' ')
        return number // 2
    else:
        print(3 * number + 1, end=' ')
        return 3 * number + 1

try:
    num = int(input('Enter a number: '))
    print(num, end=' ')
    while num != 1:
        num = collatz(num)
except ValueError:
    print('Please enter a number.')