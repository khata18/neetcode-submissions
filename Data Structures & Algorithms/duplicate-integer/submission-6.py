class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        merry = set()

        for i in nums:
            if i in merry:
                return True
            merry.add(i)
        return False