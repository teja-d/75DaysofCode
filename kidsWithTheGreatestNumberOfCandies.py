class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [False if candies[i]+extraCandies <maxCandies else True for i in range(len(candies))]