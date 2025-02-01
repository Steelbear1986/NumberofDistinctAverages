class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums=sorted(nums)
        j=0
        k=len(nums)-1
        s=set()
        while j<k:
              s.add((nums[j]+nums[k])/2)
              j+=1
              k-=1
        return len(s)