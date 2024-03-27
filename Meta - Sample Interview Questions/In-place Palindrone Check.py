"""
Write a function that returns true if a given string is a palindrome (a 
palindrome is a string that is the same when reversed, if you ignore
punctuation and capitalization).  Some examples of palindromes are:
  "Race car!"
  "A man, a plan, a canal, Panama!"
"""

text1 = "Race car!"
text2 = "A man, a plan, a canal, Panama!"
text3 = "test"

punctuation = [",", ".", "?", "!"]


def is_palindrone(text: str) -> bool:
    stripped = ""
    reversed = ""
    for char in text:
        if char.isalpha():
            stripped += char.lower()
    for i in range(len(stripped)):
        if i < 0:
            reversed += stripped[-1]
        else:
            reversed += stripped[-i - 1]

    if stripped == reversed:
        return True


print(is_palindrone(text3))


def is_palindrone1(text: str) -> bool:
    left = 0
    right = -1
    while left < len(text) / 2:
        left_letter = text[left].lower()
        if left_letter.isalpha():
            right_letter = text[right].lower()
            if right_letter.isalpha():
                if left_letter == right_letter:
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
            else:
                right -= 1
        else:
            left += 1
    return True


print(is_palindrone1(text1))
