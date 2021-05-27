# LeetCode 2. Add Two Numbers [Medium]

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        remainder = 0
        head = ListNode()
        curr = head
        l1Curr = l1
        l2Curr = l2
        # Loop through both lists and if one becomes empty before the others set the value for every node from that list to 0 for calculations
        while (l1Curr != None or l2Curr != None):
            if (l1Curr != None):
                l1Value = l1Curr.val
                l1Curr = l1Curr.next
            else:
                l1Value = 0
            if (l2Curr != None):
                l2Value = l2Curr.val
                l2Curr = l2Curr.next
            else:
                l2Value = 0
            # perform addition of values plus the carry if there is one
            calc = l1Value + l2Value + carry
            carry = int(calc / 10)
            remainder = calc % 10
            # insert the remainder into the new list
            curr.next = ListNode(remainder)
            curr = curr.next
        # if there is a remaining carry (1), insert to list
        if (carry > 0):
            curr.next = ListNode(carry)

        return head.next


def pythonLstToLinkedListNodes(lst):
    dummyHead = ListNode()
    curr = dummyHead
    for item in lst:
        curr.next = ListNode(item)
        curr = curr.next
    head = dummyHead.next
    return head


def linkedListToPythonList(head):
    curr = head
    lst = []
    while curr is not None:
        lst.append(curr.val)
        curr = curr.next
    return lst


def main():
    solution = Solution()
    tests = []

    l1 = pythonLstToLinkedListNodes([2, 4, 3])
    l2 = pythonLstToLinkedListNodes([5, 6, 4])
    tests.append(solution.addTwoNumbers(l1=l1, l2=l2))

    l1 = pythonLstToLinkedListNodes([0])
    l2 = pythonLstToLinkedListNodes([0])
    tests.append(solution.addTwoNumbers(l1=l1, l2=l2))

    l1 = pythonLstToLinkedListNodes([9, 9, 9, 9, 9, 9, 9])
    l2 = pythonLstToLinkedListNodes([9, 9, 9, 9])
    tests.append(solution.addTwoNumbers(l1=l1, l2=l2))

    for test in tests:
        print(linkedListToPythonList(test))


if __name__ == '__main__':
    main()

# Output:
# [7, 0, 8]
# [0]
# [8, 9, 9, 9, 0, 0, 0, 1]

    # Example 1:

    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [7,0,8]
    # Explanation: 342 + 465 = 807.

    # Example 2:

    # Input: l1 = [0], l2 = [0]
    # Output: [0]

    # Example 3:

    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
