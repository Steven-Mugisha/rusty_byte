class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while (True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast