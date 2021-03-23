'''
Find the highest altitude
https://leetcode.com/problems/find-the-highest-altitude/

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

 

Constraints:

    n == gain.length
    1 <= n <= 100
    -100 <= gain[i] <= 100


'''

'''
First attempt failure
'''
# class Solution(object):
#     def largestAltitude(self, gain):
#         """
#         :type gain: List[int]
#         :rtype: int
#         """
#         altitudes = [0]
#         highest_altitude = 0
#         for i in gain:
#             altitudes[i] + gain[i]
#             # highest_altitude = altitudes[i]
#         return highest_altitude

'''
Space O(n)
Time O(1)
    1. Storing current index value in an accumulator to avoid index out of range
    2. Check the accumulator's size against current max value
    3. Continue until the end then return whatever value is the max
'''

class Solution:
    def largestAltitude(self, gain) -> int:
        maxGain = 0
        accumulator = 0

        for height in gain:
            accumulator += height
            maxGain = max(maxGain, accumulator)
        return maxGain
