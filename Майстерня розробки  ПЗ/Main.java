import java.util.Random;

public class Main {
    public static void main(String[] args) {
        System.out.println("Sviastyn V.I");

        Random random = new Random();

        int[][] A = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                A[i][j] = random.nextInt(20) + 1;
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Matrix A before changes");

        int[] D = new int[3];
        for (int i = 0; i < 3; i++) {
            D[i] = random.nextInt(5) + 1; 
            System.out.print(D[i] + " ");
        }
        System.out.println("\nArray/Matrix D");

      
        for (int i = 0; i < 3; i++) {
            if ((i + 1) % 2 != 0) {
                for (int j = 0; j < 3; j++) {
                    A[i][j] = D[j];
                    System.out.print(A[i][j] + " ");
                }
            } else {
                for (int j = 0; j < 3; j++) {
                    System.out.print(A[i][j] + " ");
                }
            }
            System.out.println();
        }
        System.out.println("Matrix A after changes");

        int sum = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                sum += A[i][j];
            }
        }
        System.out.println("Sum of all elements in Matrix A: " + sum);
    }
}