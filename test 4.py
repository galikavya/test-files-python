def calculate(x, n, choice):
    operations = [x ** n, x + n, x - n, x * n, x / n if n != 0 else "Undefined"]
    return operations[choice - 1] if 1 <= choice <= 5 else "Invalid choice"

def main():
    x = float(input("X = "))
    n = float(input("N = "))
    choice = int(input("Choice (1: Pow, 2: Add, 3: Sub, 4: Mul, 5: Div) = "))
    print(f"Result = {calculate(x, n, choice)}")

if __name__ == "__main__":
    main()
