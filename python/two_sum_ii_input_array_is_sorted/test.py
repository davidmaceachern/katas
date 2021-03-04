from solution import Solution

def test_double_digits():
    """
    Test that it can return indexes for an array including double digits 
    """

    solution = Solution()
    numbers = [2,7,11,15]
    target = 9
    expected = [1,2]

    result = solution.twoSum(numbers, target)

    assert result == expected

def test_single_digits():
    """
    Test that it can return indexes for an array of only single digits 
    """

    solution = Solution()
    numbers = [2,3,4]
    target = 6 
    expected = [1,3]

    result = solution.twoSum(numbers, target)

    assert result == expected

def test_negative_target():
    """
    Test that it can return indexes for a negative number 
    """

    solution = Solution()
    numbers = [-1,0]
    target = -1 
    expected = [1,2]

    result = solution.twoSum(numbers, target)

    assert result == expected