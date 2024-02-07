"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

s = "(]"


def valid_parentheses(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] == "(" and s[i + 1] != ")":
            return False
        if s[i] == "[" and s[i + 1] != "]":
            return False
        if s[i] == "{" and s[i + 1] != "}":
            return False
    return True


print(valid_parentheses(s))

# REVIEW
# my solution works but is does not incorporate the LIFO principle

# SOLUTION


def Solution(s: str) -> bool:
    stack: list = []
    pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False

    return len(stack) == 0


print(Solution(s))
