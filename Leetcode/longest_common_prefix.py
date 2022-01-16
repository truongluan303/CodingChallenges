from typing import List


class Solution:
    
    def longest_common_prefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        
        while True:
            
            current = ""
            
            for s in strs:
                
                if i >= len(s):
                    break
                
                if current == "":
                    current = s[i]
                    
                else:
                    if current != s[i]:
                        break
            
            result += current
            i += 1

        return result