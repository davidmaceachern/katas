from solution import Solution

def test_rotates_regular_numbers():
    """
    Test that it can rotate a list of regular numbers 
    """

    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    expected = [5,6,7,1,2,3,4]

    solution.rotate(nums, k)

    assert nums == expected

def test_rotates_negative_numbers():
    """
    Test that it can rotate a list of mixed numbers 
    """

    solution = Solution()
    nums = [-1,-100,3,99]
    k = 2
    expected = [3,99,-1,-100] 

    solution.rotate(nums, k)

    assert nums == expected
