# Given a string s, return whether s is a valid number.

"""
    For example, all the following are valid numbers:
    "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",
    while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".
    """
    

s = "3e+7"

num_seen = False
dot_seen = False
e_seen = False
num_after_e = True

for i in range(len(s)):
    ch = s[i]

    if ch.isdigit():
        num_seen = True
        num_after_e = True

    elif ch == '+' or ch == '-':
        if i > 0 and s[i - 1] not in "eE":
            print(False)
            break

    elif ch == '.':
        if dot_seen or e_seen:
            print(False)
            break
        dot_seen = True

    elif ch == 'e' or ch == 'E':
        if e_seen or not num_seen:
            print(False)
            break
        e_seen = True
        num_after_e = False

    else:
        print(False)
        break

else:
    print(num_seen and num_after_e)
