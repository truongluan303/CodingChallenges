import itertools

class Solution:
    
    def letter_combinations(self, digits: str) -> list[str]:
        
        if digits == "":
            return []
        
        mapper = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        
        if len(digits) == 1:
            return mapper[digits]
        
        com = list(itertools.product(*[mapper[x] for x in digits]))
        
        return [''.join(x) for x in com]
        
        
        
        