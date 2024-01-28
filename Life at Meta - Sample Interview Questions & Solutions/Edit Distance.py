"""
Write a function that returns whether two words are 
exactly "one edit" away using the following signature:

bool OneEditApart(string s1, string s2);

An edit is:
- Inserting one character anywhere in the word (including at the beginning and end)
- Removing one character
- Replacing one character
"""


def OneEditApart(s1: str, s2: str) -> bool:
    if (len(s1) - len(s2)) > 1:
        print("More than one additional letter required")
        return False
    count = 0
    if len(s1) > len(s2):
        s2 += " "
        for i, letter in enumerate(s1):
            if letter != s2[i]:
                count += 1
    else:
        s1 += " "
        for i, letter in enumerate(s2):
            if letter != s1[i]:
                count += 1
    if count > 1:
        print("More than one letter in the wrong position")
        return False
    return True


s1 = "cat"
s2 = "cast"
print(OneEditApart(s1, s2))
