prompt = "\nPlease enter your pizza toppings, enter 'quit' to exit "

while True:
    message = input(prompt)

    if message != quit:
        print("\nI will add " + message + " to your pizza")
    else:
        break
