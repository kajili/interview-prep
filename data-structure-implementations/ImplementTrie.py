# LeetCode 208. Implement Trie (Prefix Tree) [Medium]

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(' ')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root

        for character in word:

            if character not in curr.children:
                curr.children[character] = Node(character)
            curr = curr.children[character]

        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.getNode(word)
        result = node != None and node.isWord == True

        return result

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.getNode(prefix) != None

    def getNode(self, word):
        curr = self.root

        for character in word:

            if character not in curr.children:
                return None
            curr = curr.children[character]

        return curr


class Node:

    def __init__(self, c):
        self.c = c
        self.children = {}
        self.isWord = False


def main():
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # return True
    print(trie.search("app"))  # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))  # return True


if __name__ == '__main__':
    main()

# Output:
# True
# False
# True
# True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
