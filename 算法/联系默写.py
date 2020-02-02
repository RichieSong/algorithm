# coding:utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.rigth = root.rigth, root.left
            self.invertTree(root.left)
            self.invertTree(root.rigth)
        return root

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.rigth))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if not root:
            return False
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False

        def f(root, temp=0):
            temp += root.val
            if not root.left and not root.right and sum == temp:
                return True
            if root.left: f(root.left, temp)
            if root.right: f(root.right, temp)
            return False

        return f(root)

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] for _ in range(n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                                   dp[i][j - 1] + 1, dp[i - 1][j] + 1
                                   )
        return dp[m][n]

    def test(self, nums):
        if len(nums) == 0:
            return nums
        ret = nums[0]
        maxNum = nums[0]
        minNum = nums[0]
        for i in range(1, len(nums)):
            end1, end2 = maxNum * nums[i], minNum * nums[i]
            maxNum = max(end1, end2, ret)
            minNum = min(end2, end1, ret)
            ret = max(ret, maxNum)
        return ret

    def test1(self, nums):
        len_num = len(nums)
        res = nums[0]
        for i in range(len_num):
            x = 1
            for j in range(1, len_num):
                x *= nums[j]
                if x > res:
                    res = x
        return res

    def test2(self, nums):
        maxNum = nums[0]
        cur = 0
        for i in range(len(nums)):
            cur = nums[i] if nums[i] > nums[i] + cur else nums[i] + cur
            maxNum = max(cur, maxNum)
        return maxNum
