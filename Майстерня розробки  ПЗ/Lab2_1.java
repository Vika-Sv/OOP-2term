import java.util.Random;

public class Lab2_1 {
    public static void main(String[] args) {
        Random random = new Random();

        int num4 = 1000 + random.nextInt(9000);
        int num5 = 10000 + random.nextInt(90000);

        String str4 = String.valueOf(num4);
        String str5 = String.valueOf(num5);

        System.out.println("four-digit number: " + str4);
        System.out.println("five-digit number: " + str5);

        int sum4 = calculateStringSum(str4);
        int sum5 = calculateStringSum(str5);

        int difference = sum4 - sum5;

        System.out.println("Sum of digits of the first number: " + sum4);
        System.out.println("Sum of digits of the second number: " + sum5);
        System.out.println("Difference of sums (first - second): " + difference);
    }

    public static int calculateStringSum(String s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            sum += s.charAt(i) - '0';
        }
        return sum;
    }
    
}