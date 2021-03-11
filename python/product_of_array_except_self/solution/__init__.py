'''
Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

'''
Working

Firstly return an empty list, and next think about what we need to populate it with.

Break the problem down, let's find the product of the array first.

The product is the result from multiplying each element together.

If we simply for loop then we need a way for the last element to product the rest of the list.

Nonetheless a list to append the products to and we can see what that returns.

List index out of range, thought so, next we can add a limit to stop that from happening.

Ok it's not just at the end of the array that there will be a problem finding the product.

For each item in the array we find the product of all the other members of the array except the 
actual item itself. 

Regarding the constraint, possibly required to write a test that validates that the nums[] is not out of bounds.

Solution https://leetcode.com/problems/product-of-array-except-self/solution/

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        l, r, answer = [0] * length, [0] * length, [0] * length
        l[0] = 1

        for i in range(1, length):
            l[i] = nums[i - 1] * l[i - 1]
        r[length - 1] = 1

        for i in reversed(range(length - 1 )):
            r[i] = nums[i + 1] * r[i + 1]

        for i in range(length):
            answer[i] = l[i] * r[i]
        
        return answer



        