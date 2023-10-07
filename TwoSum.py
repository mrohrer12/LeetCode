stuff = [2,2,11,15]
things = 17

class Solution():
    def twoSum(self, nums, target):
        length = len(nums)
        i = 0
        ii = 0
        Positions = [0,0]
        while i < length:
            while ii < length:
                if i != ii:
                    sum = nums[i]+nums[ii]
                    if sum == target:
                        Positions = [i,ii]
                        break
                ii += 1
            if Positions != [0,0]:
                break
            i += 1
        if Positions == [0,0]:
            print("No Combination Of Numbers Produces the Target")
        else:
            print(Positions)


tmp = Solution()
tmp.twoSum(stuff,things)