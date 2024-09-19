import re

def is_valid_username(username):
    return len(username) >= 6 and re.match(r'^[\w.@]+$', username)

def main():
    username = input("Enter the user name: ")
    reentered = input("Reenter the user name: ")
    print("User name is Valid" if username == reentered and is_valid_username(username) else "User name is Invalid")

if __name__ == "__main__":
    main()
