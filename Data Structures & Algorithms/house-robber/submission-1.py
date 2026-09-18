class Solution:
    def rob(self, nums: List[int]) -> int:
        # Example: nums = [2, 7, 9, 3, 1]
        #
        # house_value | two_back | one_back | rob_this | skip_this | best_here
        #      2      |    0     |    0     |  0+2=2   |     0     |    2
        #      7      |    0     |    2     |  0+7=7   |     2     |    7
        #      9      |    2     |    7     |  2+9=11  |     7     |    11
        #      3      |    7     |    11    |  7+3=10  |     11    |    11
        #      1      |    11    |    11    | 11+1=12  |     11    |    12
        #
        # returns 12  (robbed houses 2, 9, 1)

        best_two_back = 0   # best haul ending 2 houses before current
        best_one_back = 0   # best haul ending 1 house before current

        for house_value in nums:
            rob_this_house = best_two_back + house_value
            skip_this_house = best_one_back
            best_here = max(rob_this_house, skip_this_house)

            # slide forward one house
            best_two_back = best_one_back
            best_one_back = best_here

        return best_one_back