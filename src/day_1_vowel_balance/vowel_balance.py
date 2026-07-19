"""
## Vowel Balanace

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

- The string can contain any characters.
- The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
- If there's an odd number of characters in the string, ignore the center character.
"""

def is_balanced(s: str) -> bool:
    s = s.lower()
    vowels = "aeiou"

    l = len(s)
    first_half = s[:l//2]
    second_half = s[l//2:]
    f = 0
    sc = 0
    if l % 2 == 0:
        for i in first_half:
            if i in vowels:
                f += 1
        for i in second_half:
            if i in vowels:
                sc += 1
        if f == sc:
            return True
    else:
        for i in first_half:
            if i in vowels:
                f += 1
        for i in range(len(second_half)):
            if second_half[i] in vowels and i > 0:
                sc += 1
        if f == sc:
            return True

    return False

print(is_balanced("string"))
