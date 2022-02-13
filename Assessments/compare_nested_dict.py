import unittest



def get_diff(person1: dict, person2: dict) -> dict:
    result = dict()
    
    for key, val in person1.items():
        
        if key not in person2:
            result[key] = [val, None]
            
        elif val != person2[key]:
            
            if type(val) is dict:
                result[key] = get_diff(val, person2[key])
            
            else:
                result[key] = [val, person2[key]]
            
    
    for key, val in person2.items():
        
        if key not in person1:
            result[key] = [None, val]
            
    return result





class Test(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        
        self.person1 = {
            "name": "Hoang Truong",
            "preferred_name": "Luan",
            "age": 20,
            "address": "1 Washington Sq",
            "city": "San Jose",
            "state": "CA",
            "nationality": "Vietnam",
            "bank": {
                "name": "Chase",
                "routing_number": "0123456789",
                "account_number": "0123456789"
            }
        }
        
        self.person2 = {
            "name": "Shubham Goswami",
            "age": 21,
            "address": "1 Washington Sq",
            "city": "San Jose",
            "state": "CA",
            "nationality": "India",
            "bank": {
                "name": "Chase",
                "routing_number": "0123456789",
                "account_number": "0123456789"
            }
        }
        
        


    def test1(self):
        
        print("\nTest Case 1:")

        actual_result = get_diff(self.person1, self.person2)
        
        expected_result = {
            "name": ["Hoang Truong", "Shubham Goswami"],
            "preferred_name": ["Luan", None],
            "age": [20, 21],
            "nationality": ["Vietnam", "India"]
        }
        
        self.assertEqual(expected_result, actual_result)
        
    
    
        
    def test2(self):
        
        print("\nTest Case 2:")
        
        self.person1["bank"]["name"] = "Wells Fargo"
        self.person1["bank"]["routing_number"] = "9876543210" 
        
        actual_result = get_diff(self.person1, self.person2)
        
        expected_result = {
            "name": ["Hoang Truong", "Shubham Goswami"],
            "preferred_name": ["Luan", None],
            "age": [20, 21],
            "nationality": ["Vietnam", "India"],
            "bank": {
                "name": ["Wells Fargo", "Chase"],
                "routing_number": ["9876543210", "0123456789"]
            }
        }
        
        self.assertEqual(expected_result, actual_result)
    


if __name__ == "__main__":
    unittest.main()