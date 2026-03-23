import java.util.Random;

public class Lab2_1 {
    public static void main(String[] args) {
        Random random = new Random();

        int num4 = 1000 + random.nextInt(9000);
        int num5 = 10000 + random.nextInt(90000);

        String str4 = String.valueOf(num4);
        String str5 = String.valueOf(num5);

        System.out.println("Чотиризначне число: " + str4);
        System.out.println("П'ятизначне число: " + str5);

        int sum4 = calculateStringSum(str4);
        int sum5 = calculateStringSum(str5);

        int difference = sum4 - sum5;

        System.out.println("Сума цифр першого: " + sum4);
        System.out.println("Сума цифр другого: " + sum5);
        System.out.println("Різниця сум (перша - друга): " + difference);
    }

    public static int calculateStringSum(String s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            sum += Integer.parseInt(String.valueOf(s.charAt(i)));
        }
        return sum;
    }
}