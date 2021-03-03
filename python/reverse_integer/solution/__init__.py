class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # store the sign
        sign = '-' if x < 0 else '+'
        
        # if the sign is negative
        # slice the string
        # reverse
        # concatenate the '-'
        # convert back to int
        if sign == '-':
            i = str(x)[1:]
            reverse_i = i[::-1]
            reverse_i = int('-' + reverse_i)
        
        # convert the string
        # reverse
        # convert back to int
        else:
            i = str(x)
            reverse_i = i[::-1]
            reverse_i = int(reverse_i)
        
        # overflow checking
        if -2**31 <= reverse_i <= 2**31 - 1:
            return(reverse_i)
        else:
            return(0)