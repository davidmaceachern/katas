from solution import Solution

def test_single_duplicate():
    """
    Test that it can remove one duplicate pair 
    """

    solution = Solution()
    data = [1,1,2] 
    expected = 2 # nums = [1,2] 

    result = solution.removeDuplicates(data)

    assert result == expected

def test_multiple_duplicates():
    """
    Test that it can remove multiple duplicates 
    """

    solution = Solution()
    data = [0,0,1,1,1,2,2,3,3,4]  
    expected = 5 # nums = [0,1,2,3,4] 
    result = solution.removeDuplicates(data)

    assert result == expected

def test_no_duplicates():
    """
    Test that it can handle no duplicates 
    """
    solution = Solution()
    data = [0,1]  
    expected = 2 # nums = [0,1] 
    result = solution.removeDuplicates(data)

    assert result == expected

def test_empty_list():
    """
    Test that it can handle an empty list 
    """
    solution = Solution()
    data = []  
    expected = 0 # nums = [] 
    result = solution.removeDuplicates(data)

    assert result == expected