# CTCI Question 1.2 Check Permutation

# Given two strings,write a method to decide if one is a permutation of the other.


def checkPermutationSingleHashTable(s: str, t: str) -> bool:
    # This solution uses a single hash table and compares the second string against the hash table
    # created from the first string

    # if the strings are not the same length return false
    if len(s) != len(t):
        return False

    # build the hash map from the first string to use for comparison with second string
    # store characters of string as key and their occurences as the value
    character_values_of_first_string = {}
    for letter in s:
        if letter not in character_values_of_first_string:
            character_values_of_first_string[letter] = 1
        else:
            character_values_of_first_string[letter] += 1

    print(character_values_of_first_string)

    # loop through second string and compare to first string:
    for letter in t:

        if letter in character_values_of_first_string:
            # if the key (letter) is in the dict and if the value is not 0
            # decrement the value of the value at that key

            if character_values_of_first_string[letter] != 0:
                character_values_of_first_string[letter] -= 1
            else:
                return False
        else:
            # otherwise return false because that letter was either not in the first string
            # or the second string had an extra occurence of that letter
            return False

    # once the strings have been compared and the above loop did not return false, we know
    # the letters are permutations of eachother (anagrams)
    return True


def checkPermutationDoubleHashTable(s: str, t: str) -> bool:
    # This solution creates two hash tables, one for each string, and compares if they are equal

    string1_dict, string2_dict = {}, {}

    for char in s:
        if char in string1_dict:
            string1_dict[char] += 1
        else:
            string1_dict[char] = 1

    for char in t:
        if char in string2_dict:
            string2_dict[char] += 1
        else:
            string2_dict[char] = 1

    return string1_dict == string2_dict

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false
