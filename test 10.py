def find_mth_max_nth_min(arr, m, n):
    unique_sorted = sorted(set(arr))
    return (unique_sorted[-m], unique_sorted[n - 1]) if m <= len(unique_sorted) and n <= len(unique_sorted) else (None, None)

def main():
    arr = [14, 16, 87, 36, 25, 89, 34]
    m, n = 1, 3 
    mth_max, nth_min = find_mth_max_nth_min(arr, m, n)

    if mth_max is not None and nth_min is not None:
        print(f"{m}th Maximum Number = {mth_max}\n{n}th Minimum Number = {nth_min}")
        print(f"Sum = {mth_max + nth_min}\nDifference = {mth_max - nth_min}")
    else:
        print("Invalid M or N")

if __name__ == "__main__":
    main()
