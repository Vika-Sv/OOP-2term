import java.util.Scanner;

public class Lab2_2 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введіть ваш текст:");
        
        StringBuilder inputBuilder = new StringBuilder();
        String line;
        
        while (!(line = scanner.nextLine()).isEmpty()) {
            inputBuilder.append(line).append("\n");
        }
        
        String originalText = inputBuilder.toString().trim();

        if (originalText.isEmpty()) {
            System.out.println("Ви не ввели жодного тексту.");
            return;
        }

       
        String regex = "[\\s,.;:!?\\t\\n\\r]+";

        System.out.println("ВХІДНІ ПАРАМЕТРИ:");
        System.out.println("Введений текст:\n" + originalText);
        System.out.println("Використаний regex для спліту: " + regex);

        String[] words = originalText.split(regex);

        System.out.println("ОТРИМАНІ СЛОВА (ЛЕКСЕМИ):");
        int count = 0;
        for (String word : words) {
            if (!word.isEmpty()) {
                System.out.println(word);
                count++;
            }
        }
        
        System.out.println("\nВсього знайдено слів: " + count);
        
        scanner.close();
    }
}