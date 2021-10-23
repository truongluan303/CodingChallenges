import java.util.*;


class PascalTriangle2 {

    public static void main(String[] args) {
        List<Integer> row = getRow(3);

        for (Integer num : row) {
            System.out.print(num + " ");
        }
    }

    
    
    public static List<Integer> getRow(int rowIndex) {
        
        List<Integer> prevLevel = new ArrayList<Integer>();
        
        for (int i = 0; i <= rowIndex; i++) {
            Integer[] currentLevel = new Integer[i + 1];
            
            currentLevel[0] = 1;
            currentLevel[i] = 1;
            
            for (int j = 1; j < i; j++) {
                currentLevel[j] = prevLevel.get(j - 1) + prevLevel.get(j);
            }
            
            prevLevel = Arrays.asList(currentLevel);
        }
        
        return prevLevel;
    }
}