from solution import Solution

def test_is_a_palindrome():
    """
    Test that it can identify valid palindrome 
    """

    solution = Solution()
    string = "A man, a plan, a canal: Panama"
    expected = True 

    result = solution.isPalindrome(string)

    assert result == expected

    string = "a."
    expected = True 

    result = solution.isPalindrome(string)

    assert result == expected

def test_is_not_a_palindrome():
    """
    Test that it can identify invalid palindrome 
    """

    solution = Solution()
    string = "race a car" 
    expected = False 

    result = solution.isPalindrome(string)

    assert result == expected

    string = "a.b" 
    expected = False 

    result = solution.isPalindrome(string)

    assert result == expected