# CTCI Question 1.1 Is Unique

#  Implement an algorithm to determine if a string has all unique characters.
#  What if you cannot use additional data structures?

def isUnique_SetLengthComparison(s):
    stringSet = set(s)  # O(n) time and O(n) space

    # Compare if the set is the same length as the original string.
    # A set will only hold unique values so if they are not equal then at least one character repeated.
    isUnique = len(s) == len(stringSet)  # O(1) time

    return isUnique  # total O(n) time and O(n) space


def isUnique_SetComparingEachLetter(s):
    # Create a set and add each letter to it once.
    # return False if that character has been seen in the set before.
    stringSet = set()

    for char in s:
        if char in stringSet:
            return False
        stringSet.add(char)
    return True


def isUnique_HashTableComparingEachLetter(s):
    # Create a hash table with keys being the letters of the string and values being their number of occurrences
    # return False if value of any key goes above 1
    stringHashTable = {}

    for char in s:
        if char in stringHashTable:
            return False
        stringHashTable[char] = 1
    return True


# If we can't use additional data structures, we can do the following:
# 1. Compare every character of the string to every other character of the string.
#   This will take 0(n2) time and 0(1) space.
# 2. If we are allowed to modify the input string, we could sort the string in O(n log(n)) time and
#   then linearly check the string for neighboring characters that are identical.
#   Careful, though: many sorting algorithms take up extra space.

# These solutions are not as optimal in some respects, but might be better depending on the constraints of the problem.

def isUnique_ConstantSpace(s):
    # Sort the string
    sortedStr = "".join(sorted(s))

    # Find length of string
    n = len(s)

    # Check if neighboring characters are identical
    for i in range(1, n):
        current = sortedStr[i]
        previous = sortedStr[i - 1]

        if (current == previous):
            # if there are any values that are equal they will be next to each other after sorting
            return False
    # If we looped through and no values were equal we return True
    return True

