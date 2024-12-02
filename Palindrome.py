class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        number = x
        if number < 0:
            return False
        
        # Save the original number to compare later
        original_number = number
        reversed_number = 0

        # Reverse the number
        while number > 0:
            digit = number % 10  # Extract the last digit
            reversed_number = reversed_number * 10 + digit  # Build the reversed number
            number = number // 10  # Remove the last digit

        # Compare the reversed number with the original
        return original_number == reversed_number
