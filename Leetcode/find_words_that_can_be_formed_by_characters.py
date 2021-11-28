class Solution:
    
    def countCharacters(self, words: list, chars: str) -> int:
        
        bag = dict()
        for c in chars:
            if c not in bag:
                bag[c] = 0
            bag[c] += 1
            
            
        result = 0
            
        for word in words:
            good = True
            temp_bag = bag.copy()
            
            for c in word:
                
                if c in temp_bag:
                    temp_bag[c] -= 1
                    if temp_bag[c] == 0:
                        del temp_bag[c]
                else:
                    good = False
                    break
                    
            if good:
                result += len(word)
                
        return result
                    


solution = Solution()
print(solution.countCharacters(["cat","bt","hat","tree"], "atach"))