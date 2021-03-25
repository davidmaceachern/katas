from solution import Solution

def test_count_matches():
    """
    Test that it can count items matching the pattern 
    """

    solution = Solution()
    
    items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey = "color" 
    ruleValue = "silver"
    expected = 1

    result = solution.countMatches(items, ruleKey, ruleValue)
    assert result == expected

    items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]] 
    ruleKey = "type"
    ruleValue = "phone"
    expected = 2

    result = solution.countMatches(items, ruleKey, ruleValue)
    assert result == expected

