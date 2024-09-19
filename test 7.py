def check_voting_eligibility(age):
    if age < 0: return "Invalid input."
    return f"You are allowed to vote after {18 - age} years." if age < 18 else "You are eligible to vote."


try:
    result = check_voting_eligibility(int(input("Enter your age: ")))
except ValueError:
    result = "Invalid input."


print(result)
