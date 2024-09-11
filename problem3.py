class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x <0):
            return False

        temp = x
        rev = 0

        while(temp!=0):
            num = temp % 10
            rev = rev * 10 + num
            temp //=10
        
        return (rev == x)
        