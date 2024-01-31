class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        window = Counter()
        max_score = current_score = 0
        
        for right in range(nums.__len__()):
            window[nums[right]] += 1
            current_score += nums[right]
            
            while window[nums[right]] > 1:
                window[nums[left]] -= 1
                current_score -= nums[left]
                left += 1
                if window[nums[left]] == 0:
                    del window[nums[left]]

            
            max_score = max(current_score, max_score)

        return max_score