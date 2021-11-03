import java.util.*;


public class WoodCuttingProblem {


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n;
        int numOfCuts;

        System.out.print("\nInput length of the lumber: ");
        n = input.nextInt();

        System.out.print("\nInput number of cuts: ");
        numOfCuts = input.nextInt();

        List<Integer> cuts = new ArrayList<>();
        System.out.print("\nInput cut positions: ");
        for (int i = 0; i < numOfCuts; i++) {
            cuts.add(input.nextInt());
        }

        int minCost = calculateMinimumCost(n, cuts);
        System.out.println("\n\n==> Min Cost: $" + minCost + "\n");

        input.close();
    }




    public static int calculateMinimumCost(int n, List<Integer> cuts) {

        cuts.addAll(Arrays.asList(0, n));
        Collections.sort(cuts);

        int[][] arr = new int[cuts.size()][cuts.size()];


        for (int i = cuts.size() - 1; i >= 0; i--) {
            
            for (int j = i + 1; j < cuts.size(); j++) {

                for (int k = i + 1; k < j; ++k) {

                    int temp1 = (arr[i][j] == 0) ? Integer.MAX_VALUE : arr[i][j];
                    int temp2 = cuts.get(j) - cuts.get(i) + arr[i][k] + arr[k][j];

                    arr[i][j] = temp1;

                    if (temp2 < temp1) {
                        arr[i][j] = temp2;
                    }
                }
            }
        }
        return arr[0][cuts.size() - 1];
    }
}