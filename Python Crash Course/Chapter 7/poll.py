responses = {}

# Set flag to indicate that the polling is active

polling_activate = True

while polling_activate:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("what is your favorite basketball team? ")

    # Store the response in the dictionary

    responses[name] = response

    # Find out if anyone is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_activate = False

# Show results

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + "'s favorite basketball team is " + response + ".")
