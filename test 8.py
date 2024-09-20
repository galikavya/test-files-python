def calculate_atm_balance():
    denominations = []
    counts = []
    
    for i in range(4):
        denomination = int(input(f"Enter the {i + 1}st Denomination: "))
        count = int(input(f"Enter the {i + 1}st Denomination number of notes: "))
        denominations.append(denomination)
        counts.append(count)

    total_balance = sum(denomination * count for denomination, count in zip(denominations, counts))
    print(f"Total Available Balance in ATM: {total_balance}")

if __name__ == "__main__":
    calculate_atm_balance()
