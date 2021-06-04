# String Compression:
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not
# become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompression(string):
    # Return the string if it's length is 1 or less (since 'a' would convert to 'a1', and '' would be '').
    if len(string) <= 1:
        return string

    # Create list to append strings to instead of string concatenation.
    # Because strings are immutable in Python (and Java), it is much more efficient to append to a list and then
    # use ''.join(lst) to convert the list into a string. In Java you would use the StringBuilder class and then
    # convert it using StringBuilder.toString().
    compressed = []

    # Initialize our new string with the first value of the input string, and initialize the count value to 1.
    compressed.append(string[0])
    count = 1

    # Initialize a previous pointer to the first element of the string as well.
    prev = string[0]

    # Iterate through the string starting at the second value and compare the current values to the previous values
    for i in range(1, len(string)):
        # Initialize the current pointer to the current value of the string.
        curr = string[i]
        # Compare the current to the previous value. again.
        if curr == prev:
            # If they are the same, add 1 to the count variable and iterate again.
            count += 1
        else:
            # If the values are different, we must append the count value and then the character at the current pointer
            # to our compressed string, and then reset our count value to 1.
            compressed.extend([str(count), curr])
            count = 1
        # Update previous pointer
        prev = curr

    # Add final count to the last letter after the loop
    compressed.append(str(count))

    # Convert compressed into a string
    compressed = ''.join(compressed)
    # Return the shorter of the two strings using the min function with the key parameter with len of the strings.
    return min(string, compressed, key=len)
