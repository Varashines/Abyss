from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        t = sorted(nums)
        s = list(set(sorted(x for x in t if x>=1)))
        print(s)
        if t[-1] <= 0:
            return 1
        else:
            for i in range(1,int(s[-1])+2):
                try:
                    if (i) < int(s[i-1]):
                            #print(i+1)
                        r = i
                        return i
                except:
                    return i
                
# ... existing code ...

# Create an instance of the Solution class
solution = Solution()

# Call the method using the instance
print(solution.firstMissingPositive([1, 2, 0,1,4]))