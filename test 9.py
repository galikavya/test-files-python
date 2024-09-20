def is_palindrome(value):
    return str(value) == str(value)[::-1]

def main():
    case = int(input("Choose an option:\n1. String\n2. Number\nCase = "))
    value = input("Input = ")
    print("Palindrome" if is_palindrome(value) else "Not a palindrome")

if __name__ == "__main__":
    main()
