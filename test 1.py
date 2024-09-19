def reverse_string(s):
    r = ""
    for c in s:
        r = c + r
    return r


for case in ["TEMPLE", "SIGN UP", "AT-LEAST", "1245", "!@#$%", "145*999=144855"]:
    print(f"Input: {case} => Reversed: {reverse_string(case)}")
