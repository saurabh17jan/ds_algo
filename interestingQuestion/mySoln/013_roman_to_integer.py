# 13 Roman to Integer
# Leet
# python3

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        x = 0
        y = []
        # for x in range(len(s)):
        while(x < len(s)):
            if s[x] == 'I':
                if (x+1) < len(s) and s[x + 1] == 'V':
                    y.append(4)
                    x = x + 2
                elif (x+1) < len(s) and s[x + 1] == 'X':
                    y.append(9)
                    x = x + 2
                else:
                    y.append(1)
                    x = x + 1

            elif s[x] == 'V':
                y.append(5)
                x = x + 1

            elif s[x] == 'X':
                if (x+1) < len(s) and s[x + 1] == 'L':
                    y.append(40)
                    x = x + 2
                elif (x+1) < len(s) and s[x + 1] == 'C':
                    y.append(90)
                    x = x + 2
                else:
                    y.append(10)
                    x = x + 1

            elif s[x] == 'L':
                y.append(50)
                x = x + 1


            elif s[x] == 'C':
                if (x+1) < len(s) and s[x + 1] == 'D':
                    y.append(400)
                    x = x + 2
                elif (x+1) < len(s) and s[x + 1] == 'M':
                    y.append(900)
                    x = x + 2
                else:
                    y.append(100)
                    x = x + 1

            elif s[x] == 'D':
                y.append(500)
                x = x + 1


            elif s[x] == 'M':
                y.append( 1000)
                x = x + 1

            else:
                y.append(0)
                x = x + 1

        val = 0
        for i in y:
            val = val + int(i)
        return val
