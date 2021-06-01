# LeetCode 412. Fizz Buzz [Easy]

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int):
        answer = []

        for i in range(1, n + 1):

            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                answer.append("FizzBuzz")
            elif divisible_by_3:
                answer.append("Fizz")
            elif divisible_by_5:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer


def main():
    solution = Solution()
    tests = []
    tests.append(solution.fizzBuzz(n=3))
    tests.append(solution.fizzBuzz(n=5))
    tests.append(solution.fizzBuzz(n=15))
    for test in tests:
        print(test)


if __name__ == '__main__':
    main()

# Output:
# ['1', '2', 'Fizz']
# ['1', '2', 'Fizz', '4', 'Buzz']
# ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]

# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
