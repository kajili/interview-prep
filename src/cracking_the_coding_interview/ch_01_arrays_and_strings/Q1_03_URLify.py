# CTCI Question 1.3 URLify

# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional
# characters,and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith     ", 13
# Output: "Mr%20John%20Smith"

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
    # Convert string to list to modify indices, convert back to string before returning at the end.
    # In python this requires converting the string to a new list which still took O(n) space, so I prefer using the
    # above method which creates a new string since they both use extra space but that one is much cleaner.
    url = list(inputString)

    # Count the number of spaces
    spaceCount = 0
    for charIndex in range(0, trueLength):
        currentChar = url[charIndex]
        if currentChar == ' ':
            spaceCount += 1

    # Create new index based on allocated number of spaces plus trueLength
    # (which is trueLength + (spaceCount * 2) because the trueLength contains the original spaces as well,
    # so we allocate two extra places for each '%20' symbol compared to the ' ' space).
    newIndex = trueLength + (spaceCount * 2)

    # Iterate backwards through the full string and if there is a space, replace the values for spaces with '%20'
    # otherwise move any other character to the required index.
    for charIndex in reversed(range(trueLength)):
        if url[charIndex] == ' ':
            url[newIndex - 3] = '%'
            url[newIndex - 2] = '2'
            url[newIndex - 1] = '0'
            newIndex -= 3
        else:
            url[newIndex - 1] = url[charIndex]
            newIndex -= 1

    # Convert back to a string and strip trailing whitespace
    # *reference for string strip(), rstrip(), and lstrip() functions:
    #   https://www.journaldev.com/23625/python-trim-string-rstrip-lstrip-strip
    url = "".join(url).rstrip()

    return url


if __name__ == '__main__':
    print(URLify_InPlace('test string       ', 11))
