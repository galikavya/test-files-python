def calculate(x, n, choice):
    return (x**n if choice == 1 else
            x+n if choice == 2 else
            x-n if choice == 3 else
            x*n if choice == 4 else
            (x/n if n else "Undefined") if choice == 5 else "Invalid choice")

x = float(input("Enter X: "))
n = float(input("Enter N: "))
choice = int(input("Choice (1: Pow, 2: Add, 3: Sub, 4: Mul, 5: Div): "))

print(f"Result: {calculate(x, n, choice)}")

for x, n in [(0, 4), (5, 0), (-3, 3), (0, 0), (123, 123)]:
    print(f"X = {x}, N = {n} => Add: {x+n}, Sub: {x-n}, Mul: {x*n}, Div: {x/n if n else 'Undefined'}, Pow: {x**n}")
