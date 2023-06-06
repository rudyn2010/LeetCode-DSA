# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #Driver Code for in-order DFS - the "thing" that will check our values
        def dfs(node, currSum):
            
            #Base Case: Given an empty tree we return False (ex. 3)
            if not node:
                return False
            
            currSum += node.val
            
            #Leaf node if no left or right children, return boolean if condition is met 
            if not node.left and not node.right:
                return currSum == targetSum 
             
            #Recursive step to check in order all paths, left to right 
            return (dfs(node.left, currSum) or 
                   dfs(node.right, currSum))
        
        #Driver code passing in our first root node, and initial currSum of 0. 
        return dfs(root, 0)