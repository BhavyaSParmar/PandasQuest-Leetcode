class Solution:
    def countHillValley(self, nums: List[int]) -> int:
         filtered = [nums[0]]
         for n in nums[1:]:
            if n != filtered[-1]:
                filtered.append(n)

         count = 0
         for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  # hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1  # valley

         return count