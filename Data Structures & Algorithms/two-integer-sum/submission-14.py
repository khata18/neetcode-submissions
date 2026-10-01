class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in self.map:
                return [self.map[diff],i]
            self.map[n] = i