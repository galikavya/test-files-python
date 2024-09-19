def reverse_number(num):
    num_str = str(num).strip()
    if not num_str.lstrip('-').isdigit():
        return "Invalid input."
    
    reversed_num = int(num_str[::-1])
    return -reversed_num if num_str[0] == '-' else reversed_num


user_input = input("Number: ")
result = reverse_number(user_input)


print(f"Reverse Number: {result}")
