# Jonathan Lopez
# 11/22/2024

from typing import List, Optional


def problem1():
    # write an infinite while loop
    i = 1
    while i == 1:
         print("infinite")
    
def problem2():
    """
    Using a while loop, create a list called L that contains the numbers 0 to 10. On each
    iteration, the loop should append the current value of a counter variable to the list and then
    increase the counter by 1. The while loop should stop once the counter variable is greater than
    10
    """
    count = 0
    L = []
    while (count <= 10):
         L.append(count)
         count = count + 1
    print(L)
    
def problem3():
    """
    Using a while loop, ask the user to enter a number. Append each entered number
    to a list and add them together. Continue asking for a number until the sum of the list of
    numbers is greater than 100.
    """
    count = 0
    L = []
    while (count <= 100):
        V = int(input("Enter a number")) 
        L.append(V)
        count = count + V
    print(count)
    
def problem4():
    """
    Create a while loop that initializes a counter at 0 and will run until the counter
    reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
    Confirm the list results using a print statement.
    """
    count = 0
    tens = []
    while (count <= 50):
        if count % 10 == 0:
            tens.append(count)
        count = count + 1
    print(tens)

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isMirror(self, root: Optional[TreeNode]) -> bool:
        # source: https://leetcode.com/problems/symmetric-tree/description/?envType=problem-list-v2&envId=binary-tree
        # check if the binary tree is a mirror of itself
        # a tree is symetric if it is a mirror of it self, return true if it is.
        """
             1
           /   \\
          2     2
         / \   / \\
        3   4 4   3
        
        For example, the tree above, if the right subtree and left subtree replaces each other it would still be the same
        
        
                1
              /   \\
             2     2
             \      \\
              3      3
        But not this one, when swapping them, it would results in the different tree
        To earn credit for this problem
        you must:
        1. solve it succesfully, pass all test cases on leetcode
        2. explain in high details with your though process
        If you don't satisfy the requirement then you will not receive credit for this problem
        """
        
def findRelativeRanks(self, score: List[int]) -> List[str]:
    # https://leetcode.com/problems/relative-ranks/?envType=problem-list-v2&envId=heap-priority-queue
    # Same requirments as above
    # each of this problem will have 15 extra credit
        ...
        
if __name__ == "__main__":
    problem4()
