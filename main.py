class Solution:
    def romanToInt(self, s: str) -> int:
        # converts a string of a roman numeral to an integer.
        l = []
        for char in s:
            if char == "I":
                l.append(1)
            elif char == "V":
                l.append(5)
            elif char == "X":
                l.append(10)
            elif char == "L":
                l.append(50)
            elif char == "C":
                l.append(100)
            elif char == "D":
                l.append(500)
            elif char == "M":
                l.append(1000)
        total = 0
        y = 1
        for x in l:
            if y == len(l):
                total += x
            elif x >= l[y]:
                total += x
            else:
                total -= x
            y += 1

            
        return total

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # returns the index of 2 numbers that combined equal the target number (index 1 and index 2 cannot be equal to eachother)
        x = 0
        for x1 in nums:
            y = 0
            for y1 in nums:
                if x1 + y1 == target and x != y:
                    return [x, y]
                y += 1
            x += 1
    
    def isPalindrome(self, x: int) -> bool:
        # checks if a number is a palindrome(when reversed is the same)
        x = str(x)
        y = 0
        for _ in range(len(x)):
            if x[y] != x[-y - 1]:
                return False
            y += 1
        return True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        y = 0
        for c in strs[0]:
            for word in strs:
                try:
                    if word[y] != strs[0][y]:
                        return ret
                except:
                    return ret
            ret += c
            y += 1
        return ret
