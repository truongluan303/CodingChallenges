LEFT = {'[', '(', '{'}
RIGHT = {']', ')', '}'}
PAREN_MAP = {'(':')', '{':'}', '[':']'}


class Solution:
    
    def is_valid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:
            
            if c in LEFT:
                
                stack.append(c)
                
            elif c in RIGHT:
                
                if len(stack) == 0:
                    return False
                
                left = stack.pop()
                
                if PAREN_MAP[left] != c:
                    return False
                
        if len(stack) != 0:
            return False
                
        return True