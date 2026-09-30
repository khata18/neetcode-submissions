class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashnum = []
        for digit in nums:
            if digit in hashnum:
                return True
            else:
                hashnum.append(digit)

        return False

            
            
        