VALUES = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


class Solution:

    def romanToInt(self, s: str) -> int:

        result = 0
        i = 0
        
        while i < len(s):
            
            current_val = VALUES[s[i]]
            
            if i < len(s) - 1:
                
                next_val = VALUES[s[i + 1]]

                if current_val < next_val:
                    result += next_val
                    result -= current_val
                    i += 1
                
                else:
                    result += current_val
                    
            else:
                result += current_val

            i += 1
                
                
        return result