from solution import Solution

def test_largest_altitude():
    """
    Test that it can find the highest altitude 
    """

    solution = Solution()

    gain = [-5,1,5,0,-7]
    expected = 1

    result = solution.largestAltitude(gain)

    assert result == expected

    gain = [-4,-3,-2,-1,4,3,2]
    expected = 0

    result = solution.largestAltitude(gain)

    assert result == expected