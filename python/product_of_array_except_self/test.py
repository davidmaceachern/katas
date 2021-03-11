from solution import Solution

def test_product_except_self():
    """
    Test that it can find the product except self 
    """

    solution = Solution()

    nums = [1,2,3,4]

    expected =  [24,12,8,6]

    result = solution.productExceptSelf(nums)

    assert result == expected

# def test_product_except_self_large_int():
#     """
#     Test that it can return a 0 if outside 32bit integer range
#     """
#     solution = Solution()

#     # data = 2147483647

#     nums = []

#     result = solution.productExceptSelf(data)

#     assert result == 0