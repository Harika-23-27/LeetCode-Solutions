class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target = k * threshold
        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= target:
            count += 1

        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]

            if window_sum >= target:
                count += 1

        return count



