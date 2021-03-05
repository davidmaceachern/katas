'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
'''

'''
First attempt does not pass all test cases

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = s.lower().replace(" ", "").replace(",", "").replace(":", "").replace(".", "").replace("@", "").replace("#","")
        palindrome = string[::-1]
        if(string == palindrome):
            return(True)
        else:
            return(False)
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from string import digits, ascii_uppercase, ascii_lowercase

        if not s:
            return True
        
        valid_char = digits + ascii_lowercase
        i = 0 
        j = len(s) - 1

        # same speed pointers left and right using while loop
        while i <= len(s) - 1 and j >= 0 and i < j:
            # using each pointer check validity of character
            while s[i].lower() not in valid_char and i < len(s) - 1 and i < j:
                i += 1
            while s[j].lower() not in valid_char and j > 0 and j > i:
                j -= 1
            # then check that each valid character is also equal
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True