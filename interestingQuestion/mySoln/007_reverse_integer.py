#7 Reverse Integer
#Leet
#Given a 32-bit signed integer, reverse digits of an integer.
#Note:
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2pow(31),  2pow(31) − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
    # def reverse( x: int) -> int:
        if x >= 0:
            num_str = str(x)
            i = 0
            s = ""
            for ch in num_str:
                s = ch + s
            
            if int(s) == 'None' or int(s) > 2147483648 or int(s) < -2147483647:
                return 0
            else:
                return int(s)
        
        else:
            num_str1 = str(x)
            s = ""
            i = 0
            num_str = num_str1[1:]
            for ch in num_str:
                s = ch + s
            
            if int(s)*(-1) == 'None' or int(s)*(-1) > 2147483648 or int(s)*(-1) < -2147483647:
                return 0
            else:
                return int(s)*(-1)
        
