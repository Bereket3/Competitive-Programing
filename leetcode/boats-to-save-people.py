class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = out = 0
        right = len(people) - 1
        while right >= left:
            if people[left] + people[right] <= limit:
                left += 1
            out += 1
            right -= 1
        
        return out