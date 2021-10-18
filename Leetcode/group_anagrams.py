class Solution:

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        
        dictionary = dict()
        existed_keys = set()
        
        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in existed_keys:
                existed_keys.add(key)
                dictionary[key] = []
                
            dictionary[key].append(word)
                
        return dictionary.values()