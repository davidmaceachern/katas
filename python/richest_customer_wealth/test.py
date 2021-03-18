from solution import Solution 

def test_maximum_wealth():
    """
    Test that it can identify the richest customer 
    """

    solution = Solution()

    accounts = [[1,2,3],[3,2,1]]

    expected = 6 

    result = solution.maximumWealth(accounts)

    assert result == expected

    accounts = [[1,5],[7,3],[3,5]]

    expected = 10

    result = solution.maximumWealth(accounts)

    assert result == expected

    accounts = [[2,8,7],[7,1,3],[1,9,5]]

    expected = 17

    result = solution.maximumWealth(accounts)

    assert result == expected