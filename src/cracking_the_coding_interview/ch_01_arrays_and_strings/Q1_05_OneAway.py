# CTCI Question 1.5 One Away

# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def oneAway(str1, str2):
    lengthDifferenceOverOne = abs(len(str1) - len(str2)) > 1
    if lengthDifferenceOverOne:
        return False

    # If strings are dif lengths, get the shorter and longer strings.
    if len(str1) < len(str2):
        shorter = str1
        longer = str2
    else:
        shorter = str2
        longer = str1

    indexShorter = 0
    indexLonger = 0
    countDiff = 0

    while (indexShorter < len(shorter) and indexLonger < len(longer)):

        if shorter[indexShorter] != longer[indexLonger]:
            # Increase the number of differences found
            countDiff += 1
            # Return false if we found more than one difference
            if countDiff > 1:
                return False

            if len(shorter) == len(longer):
                # If the strings are not the same length then increment the longer one
                indexLonger += 1
            else:
                # If the strings are the same length increment both pointers
                indexShorter += 1
                indexLonger += 1
        else:
            # If the characters are the same increment both pointers.
            indexShorter += 1
            indexLonger += 1

    return True
