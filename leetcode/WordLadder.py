# LeetCode 127. Word Ladder

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # Store the word list as a set for constant lookup time
        wordSet = set(wordList)

        # Check if the endWord exists within the wordSet and if not then return 0 because
        # the path won't be possible in this case.
        if endWord not in wordSet:
            return 0

        # Create a queue and a visited set for exploring the bfs.
        queue = []
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        # Create a result counter that starts at 1 because we are already looking at the first word (beginWord)
        result = 1

        # Create a string that contains the alphabet so we can replace values using this string
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        # Perform bfs through the elements at the top of the queue
        # while checking if each word with a single letter replaced exists
        # within the wordSet.
        while queue:
            # loop through the size of the queue and within this loop we will enqueue each connected node
            size = len(queue)
            for i in range(size):
                # for each word in the queue we must pop that value and then
                # replace every letter and check if it's within the wordSet
                word = queue.pop(0)

                # if word is equal to endWord, we return our result value plus one because we traverse again.
                if word == endWord:
                    return result

                for index in range(len(word)):
                    # This loop takes a constant 26 loops
                    for a in alphabet:
                        if a != word[index]:
                            newWord = word[0:index] + a + word[index + 1:]

                            # Another simpler to understand yet slower method of replacing the letters in the word
                            #   is in this comment below.
                            # newWord = list(word)
                            # newWord[index] = a
                            # newWord = "".join(newWord)

                            # if newWord is in the wordSet and has not been visited yet
                            # we will add the word to the queue and the visited set.
                            #   this is because that implies this is a connected node to the node we are looking
                            #   at from the queue, and has not been visited yet. So we need to mark it as visited
                            #   and add it to the queue so that we can check it's connected nodes
                            if newWord in wordSet and newWord not in visited:
                                queue.append(newWord)
                                visited.add(newWord)

            result += 1

        # Return 0 if the bfs loop never returned a value because the path did not exist
        return 0


def main():
    solution = Solution()
    test = solution.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
    print(test)

if __name__ == '__main__':
    main()

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
