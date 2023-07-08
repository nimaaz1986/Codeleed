class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for i in reversed(s):
            current_value = roman_to_int[i]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        return total


sol = Solution()
print(sol.romanToInt('III'))  # prints: 3
print(sol.romanToInt('LVIII'))  # prints: 58
print(sol.romanToInt('MCMXCIV'))  # prints: 1994


# class Solution(object):
#     def romanToInt(self, s):
#         roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         number=0
#         for i in range(len(s)-1):
#             if roman[s[i]] < roman[s[(i+1)]]:
#                 number -= roman[s[i]]
#             else:
#                 number += roman[s[i]]
#         return number + roman[s[-1]]
