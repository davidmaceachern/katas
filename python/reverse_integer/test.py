from solution import Solution

def test_reverse_basic_int():
    """
    Test that it can reverse a basic integer 
    """
    solution = Solution()
    data = 12
    result = solution.reverse(data)
    assert result == 21

def test_reverse_negative_int():
    """
    Test that it can reverse a negative integer 
    """
    solution = Solution()
    data = -12
    result = solution.reverse(data)
    assert result == -21

def test_reverse_large_int():
    """
    Test that it can return a 0 if outside 32bit integer range
    """
    solution = Solution()
    data = 2147483647
    result = solution.reverse(data)
    assert result == 0
