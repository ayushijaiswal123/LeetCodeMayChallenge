class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        biggest = float('-inf')
        to_return = 0
        print(count)
        for c in count:
            if count[c] > biggest:
                print(c, count[c])
                to_return = c
                biggest  = count[c]
                
        return to_return
