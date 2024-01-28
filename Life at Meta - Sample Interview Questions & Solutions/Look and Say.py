"""
Implement a function that outputs the Look and Say sequence:

1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
"""


def look_and_say(numbers: str):
    cycles = 5
    for _ in range(cycles):
        if len(numbers) == 1:
            print(numbers)
            numbers += "1"
            print(numbers)
            cycles -= 1
        numbers = calculate(numbers)
        print(numbers)
        cycles -= 1


def calculate(numbers):
    new_numbers = ""
    count = 0
    looking_for = numbers[0]
    for i, number in enumerate(numbers):
        if number == looking_for:
            count += 1
        if looking_for != number:
            new_numbers += f"{count}{looking_for}"
            looking_for = number
            count = 1
    new_numbers += f"{count}{looking_for}"
    return new_numbers


look_and_say("1")
