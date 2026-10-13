number = int (input ("Enter your number : "))

first = 0
second = 1
n = 2

def fibo (first, second, number, n):
    if number == 0:
        return 0
    if number == 1 or number == 2:
        return 1
    if n > number:
        return second
    if n <= number:
        temp = second
        second = first + second
        first = temp
    return fibo (first, second, number, n + 1)

print (fibo (first, second, number, n))
