string = input ("Enter your word : ")
left = 0
right = len (string) - 1

def Palindrome (left, right, string):
    if left >= right:
        return True
    if string [left] != string [right]:
        return False
    else:
        return Palindrome (left + 1, right - 1, string)

print (Palindrome (left, right, string))