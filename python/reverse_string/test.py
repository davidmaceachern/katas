from solution import Solution

def test_reverse_string():
    """
    Test that it can reverse a string 
    """

    solution = Solution()
    data = ["h","e","l","l","o"]
    expected = ["o","l","l","e","h"]

    result = solution.reverseString(data)

    assert result == expected

def test_reverse_anagram():
    """
    Test that it can reverse an anagram 
    """

    solution = Solution()
    data =  ["H","a","n","n","a","h"]
    expected = ["h","a","n","n","a","H"]
    result = solution.reverseString(data)

    assert result == expected
