# Start a formula that takes in the string of variables.
# Iterate over the characters in the string.
# Keep track of each of the types of characters, + for open, - for close.
# Check the values for each of the characters to see if they are 0 or not.
# If all are zero, return true.
# If not zero, return false.
# return character_counter + character_counter + character_counter == 0


def balancedBrackets(string):
    array = list(string)

    stack = []

    openers = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    closers = ["}", "]", ")"]

    for c in array:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if openers[stack.pop()] != c:
                return False

    return len(stack) == 0


print(balancedBrackets('{}[]()'))        # should print True
print(balancedBrackets('{(([]))}'))      # should print True
print(balancedBrackets('{ [ ] ( ) }'))   # should print True
print(balancedBrackets('{ [ ( ] ) }'))   # should print False
print(balancedBrackets('('))             # should print False
print(balancedBrackets('{[}'))           # should print False
