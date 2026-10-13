array = []

length = int (input ("Enter number of elements in array : "))

for i in range (0, length):
    element = int (input (f"Enter the element {i + 1} : "))
    array.append (element)

def SelectionSort (array):
    for i in range (0, length - 1):
        minimum = array [i]
        for j in range (i + 1, length):
            if minimum > array [j]:
                minimum = j                  
        array [i], array [minimum] = array [minimum], array [i]
                
