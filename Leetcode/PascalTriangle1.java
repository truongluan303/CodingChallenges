import java.util.*;


class PascalTriangle1 {

    public static void main(String[] args) {
        List<List<Integer>> nums = generate(5);

        for (List<Integer> level : nums) {
            for (Integer num : level) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }


    
    public static List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < numRows; i++) {
            Integer[] level = new Integer[i + 1];
            
            level[0] = 1;
            level[i] = 1;
            
            for (int j = 1; j < i; j++) {
                level[j] = result.get(i - 1).get(j - 1) + result.get(i - 1).get(j);
            }
            result.add(Arrays.asList(level));
        }
        return result;
    }
}