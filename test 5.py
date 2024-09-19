def find_mth_max_nth_min(arr, M, N):
    unique_sorted = sorted(set(arr))
    mth_max = unique_sorted[-M] if 1 <= M <= len(unique_sorted) else None
    nth_min = unique_sorted[N - 1] if 1 <= N <= len(unique_sorted) else None
    return mth_max, nth_min

def sum_diff(mth_max, nth_min):
    return (mth_max + nth_min, mth_max - nth_min) if mth_max and nth_min else (None, None)


test_cases = [({16}, 0, 1), ({0}, 1, 2), ({-12, -78, -35, -42, -85}, 3, 3), 
              ({15, 19, 34, 56, 12}, 6, 3), ({85, 45, 65, 75, 95}, 5, 7)]

for arr, M, N in test_cases:
    mth_max, nth_min = find_mth_max_nth_min(arr, M, N)
    total_sum, total_diff = sum_diff(mth_max, nth_min)
    print(f"Array: {arr}, M: {M}, N: {N} -> Mth max: {mth_max}, Nth min: {nth_min}, Sum: {total_sum}, Diff: {total_diff}")

