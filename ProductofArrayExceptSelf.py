class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = nums
        temp = list(map(lambda x: 1 if x==0 else x,temp))
        print(temp)
        total = prod(temp)
        out = []
        if 0 in nums:
            if nums.count(0)>1:
                out = [0]*len(nums)
            else:
                out = [0]*len(nums)
                out[nums.index(0)]=total
        else:
            out = [int(total/nums[i]) for i in range(len(nums))]
        return out