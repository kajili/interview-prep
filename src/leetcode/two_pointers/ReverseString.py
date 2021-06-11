# LeetCode 344. Reverse String [Easy]

# Write a function that reverses a string. The input string is given as an array of characters s.
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        start = 0
        end = n - 1

        while start < end:
            # Swap elements
            s[start], s[end] = s[end], s[start]
            # Increment start pointer and decrement end pointer
            start += 1
            end -= 1

        return s
