class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashnum = {}
        for digit in nums:
            if digit in hashnum:
                return true
            else:
                hashnum.append(digit)

        return false

            
            
        