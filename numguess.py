import random
cnumber = random.randrange(1,101)
user_input = int(input("Enter your number->>"))
if user_input>cnumber:
    print("Computer number",cnumber)
    print("Your guess number is too high")
elif user_input<cnumber:
    print("Computer number", cnumber)
    print("Your guess number is too low")
elif user_input == cnumber:
    print("Computer number", cnumber)
    print("Your guess number is matched with cnumber")