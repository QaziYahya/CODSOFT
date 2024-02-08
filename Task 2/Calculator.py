op = None
res = None

while True:
    print("Enter + for Addition.")
    print("Enter - for Subtraction.")
    print("Enter * for Multiplication.")
    print("Enter / for Division.")
    print("Enter q to quit.")
    op = input("Select an option > ")

    if op == "q":
        break

    elif op not in ('+', '-', '*', '/'):
        print()
        print("Enter a valid option!")
        print()
        continue

    while True:
        try:
            print()
            num_1 = int(input("Enter the first number: "))
            num_2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if op == '+':
        res = num_1 + num_2
    elif op == '-':
        res = num_1 - num_2
    elif op == '*':
        res = num_1 * num_2
    elif op == '/':
        if num_2 == 0:
            print()
            print("Cannot divide by Zero!")
            print()
            continue
        res = num_1 / num_2

    print()
    print(f"{num_1} {op} {num_2} = {res}")
    print()