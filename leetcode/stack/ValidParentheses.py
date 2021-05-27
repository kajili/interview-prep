# LeetCode 20. Valid Parentheses [Easy]

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            # check if character is closed parentheses
            if char in mapping:
                if stack:
                    # If the stack is not empty on a closed parentheses, then we must check if the value of the closed parentheses is equal to the type of open parentheses from the top of the stack
                    if stack.pop() != mapping[char]:
                        return False
                else:
                    # If the stack is empty on a closed parentheses, then there is no corresponding open parentheses and the input is invalid
                    return False
            else:
                # if character is open parentheses just add to stack
                stack.append(char)

        # return true if stack is empty and false otherwise. if the stack is not empty at the end of the loop then there is a dangling open parentheses with no correponding closed parentheses and therefore is invalid.
        return not stack


def main():
    solution = Solution()
    tests = []
    tests.append(solution.isValid(s="()"))
    tests.append(solution.isValid(s="()[]{}"))
    tests.append(solution.isValid(s="(]"))
    tests.append(solution.isValid(s="([)]"))
    tests.append(solution.isValid(s="{[]}"))
    print(tests)


if __name__ == '__main__':
    main()

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Example 4:

# Input: s = "([)]"
# Output: false

# Example 5:

# Input: s = "{[]}"
# Output: true
