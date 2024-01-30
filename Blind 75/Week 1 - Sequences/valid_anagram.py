"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

# at first glance it seems like you could convert each char in the string to an int,
# add them all up, then check for equality
# but this is going to mean you have to loop over both strings to convert them
# maybe a hash? I would need Google for that + a lib so I will try that after for now I will do it my way
s: str = "anagram"
t: str = "nagaram"


def validAnagram(s, t) -> True:
    # doing weirdness to try and reduce loops to 1
    st = s + t
    s_ = 0
    t_ = 0
    for idx, letter in enumerate(st):
        if idx < len(s):
            s_ += int(ord(letter))
        else:
            t_ += int(ord(letter))
    if s_ == t_:
        return True
    else:
        return False


# print(validAnagram(s, t))

print(hash(s) == hash(t))
