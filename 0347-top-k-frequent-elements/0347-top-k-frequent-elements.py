class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        freq = [[] for i in range(len(nums) + 1)]


        # Sets up a dictionary where the key is the num and the value is the count
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
    
        for key, value in counts.items():
            freq[value].append(key)

        res = []
        for tup in freq[::-1]:
            for n in tup:
                res.append(n)
                if len(res) == k:
                    return res