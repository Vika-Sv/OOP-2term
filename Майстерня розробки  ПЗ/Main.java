import java.util.Random;

public class Main {
    public static void main(String[] args) {
        System.out.println("Sviastyn V.I");

        Random random = new Random();

        // Ініціалізація та заповнення матриці A
        int[][] A = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                // nextInt(20) дає 0-19, тому додаємо 1, щоб отримати 1-20
                A[i][j] = random.nextInt(20) + 1;
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Matrix A before changes");

        // Ініціалізація та заповнення масиву D
        int[] D = new int[3];
        for (int i = 0; i < 3; i++) {
            D[i] = random.nextInt(5) + 1; // Діапазон 1-5
            System.out.print(D[i] + " ");
        }
        System.out.println("\nArray/Matrix D");

        // Модифікація матриці A (заміна непарних рядків елементами з D)
        for (int i = 0; i < 3; i++) {
            // В програмуванні індекси з 0, тому (i + 1) робить 1-й рядок непарним
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

        // Обчислення суми
        int sum = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                sum += A[i][j];
            }
        }
        System.out.println("Sum of all elements in Matrix A: " + sum);
    }
}