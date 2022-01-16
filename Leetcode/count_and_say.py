def count_and_say(n: int) -> str:
    
    result = "1"
    
    for _ in range(1, n):
        
        temp = ""
        
        prev = result[0]
        
        count = 1
        
        for i in range(1, len(result)):
            
            if result[i] == prev:
                count += 1
                
            else:
                temp += str(count)
                temp += str(prev)
                
                prev = result[i]
                count = 1
                
        temp += str(count)
        temp += str(prev)
    
        result = temp
        
    return result




if __name__ == "__main__":

    for i in range(1, 10):
        print(count_and_say(i))