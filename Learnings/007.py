x = input ("Enter your word/number : ")
n = int (input ("How many times you want to print : "))

def function (x, n):
    if n == 0:
        return
    print (f"{n}. {x}")
    function (x, n - 1)
    print (f"{n}. {x}")

function (x, n)