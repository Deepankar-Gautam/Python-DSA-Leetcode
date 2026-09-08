array = []

l = int (input ("Enter the length of array : "))
for i in range (0, l):
    n = (int (input (f"Enter your {i+1} value : ")))
    array.append(n)

left = int (input ("Enter your min value in terms of indexing : "))
right = int (input ("Enter your max value in terms of indexing : "))

def RevArray (min, max, array):
    if min >= max:
        return
    array [min], array [max] = array [max], array [min]
    return RevArray (min + 1, max - 1, array)

print (array)
y = RevArray(left, right, array)
print (array)