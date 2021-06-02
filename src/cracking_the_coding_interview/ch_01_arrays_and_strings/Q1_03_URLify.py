# CTCI Question 1.3 URLify

# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional
# characters,and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

def URLify_NewString(inputString, trueLength):
    # Create new string for string concatenation
    url = ""

    # Loop through inputString based on the true length and add each character to new string
    # except when the character is a space, then we add %20 instead.
    for charIndex in range(0, trueLength):
        if inputString[charIndex] != ' ':
            url += inputString[charIndex]
        else:
            url += '%20'

    return url


def URLify_InPlace(inputString, trueLength):
    pass
    # return inputString

# EXAMPLE
# Input: "Mr John Smith     ", 13
# Output: "Mr%20John%20Smith"
