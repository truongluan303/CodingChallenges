class RotateImage {

    public static void main(String[] args) {
        int[][] matrix = new int[][]{{5,1,9,11}, {2,4,8,10}, {13,3,6,7}, {5,14,12,16}};

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();

        rotate(matrix);

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    
    


    public static void rotate(int[][] matrix) {
        
        int size = matrix.length;
        
        for (int i = 0; i < size / 2; i++) {
            
            for (int j = i; j < size - i - 1; j++) {
                
                int temp = matrix[i][j];
                matrix[i][j] = matrix[size - j - 1][i];
                matrix[size - j - 1][i] = matrix[size - i - 1][size - j - 1];
                matrix[size - i - 1][size - j - 1] = matrix[j][size - i- 1];
                matrix[j][size - i- 1] = temp;
            }
        }
    }
}