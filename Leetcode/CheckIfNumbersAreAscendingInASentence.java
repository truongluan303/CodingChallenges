import java.util.*;


class CheckIfNumbersAreAscendingInASentence {
    
    private HashSet<Character> numbers = new HashSet<>(
        Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')    
    );
    
    
    
    public boolean areNumbersAscending(String s) {
        
        int prevNum = -1;
        String temp = "";
        
        for (int i = 0; i < s.length(); i++) {
            
            if (numbers.contains(s.charAt(i))) {
                temp += s.charAt(i);
                
                if (i == s.length() - 1 || !numbers.contains(s.charAt(i + 1))) {
                    int num = Integer.parseInt(temp);
                    
                    if (num <= prevNum) {
                        return false;
                    }
                    temp = "";
                    prevNum = num;
                }
            }
        }
        return true;
    }
}