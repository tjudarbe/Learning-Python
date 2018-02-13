count = 0
total = 0

while True:
    value = input('Enter a Number: ')
    if value == 'done':
        break
    try:
        finalValue = float(value)

    except:
        print('Invalid Input')
        continue

    count = count + 1
    total = total + finalValue


print(total, count, total/count)
