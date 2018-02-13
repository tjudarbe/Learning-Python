numbers = [4, 5, 7]
original_number = -1
smallest = None

for number in numbers:
    if number > original_number:
        original_number = number
    if smallest is None :
        smallest = number
    elif number < smallest:
        smallest = number

print("The largest number in the list is: ", original_number)
print("The smallest number in the list is: ", smallest)
