class Solution:
    def findMaxLength(self, nums) -> int:
        counts  = {}
        max_length = 0
        count = 0
        counts[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
                
            if count in counts:
                max_length = max(max_length, i-counts[count])
            else:
                counts[count] = i
        return max_length
    # * Top 94%, Solution explained by Nick White 