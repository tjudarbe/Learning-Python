prompt = "How old are you?"
prompt += "\nEnter quit when you are finished "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("The ticket is free\n")
    elif age < 13:
        print("The price of the ticket is $10\n")
    else:
        print("The price of the ticket is $15\n")
