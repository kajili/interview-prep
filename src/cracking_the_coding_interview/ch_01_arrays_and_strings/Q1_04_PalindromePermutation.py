# CTCI Question 1.4 Palindrome Permutation

# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

def palindromePermutation(string):
    # preprocess the string to all lowercase and remove spaces
    string = string.lower().replace(' ', '')

    # generate hash table with characters as keys and number of occurrences as values
    palindrome_hash_map = {}

    for char in string:
        if char not in palindrome_hash_map:
            palindrome_hash_map[char] = 1
        else:
            palindrome_hash_map[char] += 1

    # iterate through hash table and store a countOddValue counter, if it goes above 1 then return False
    countOddValue = 0

    for char in palindrome_hash_map:
        isOdd = palindrome_hash_map[char] % 2 != 0

        if isOdd:
            countOddValue += 1
        if countOddValue > 1:
            return False

    return True
