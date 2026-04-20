import java.util.Scanner;

public class Lab2_2 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your text:");
        
        StringBuilder inputBuilder = new StringBuilder();
        String line;
        
        while (!(line = scanner.nextLine()).isEmpty()) {
            inputBuilder.append(line).append("\n");
        }
        
        String originalText = inputBuilder.toString().trim();

        if (originalText.isEmpty()) {
            System.out.println("You haven't entered any text.");
            return;
        }

        String[] sentences = originalText.split("[.!?]+");
        int sentenceCount = 0;
        for (String s : sentences) {
            if (!s.trim().isEmpty()) {
                sentenceCount++;
            }
        }
        
        if (sentenceCount < 2) {
            System.out.println("Text must consist of at least two sentences.");
            return;
        }

        String regex = "[\\s,.;:!?\\t\\n\\r]+";

        System.out.println("\nPARAMETERS:");
        System.out.println("Entered text:\n" + originalText);
        System.out.println("Used regex for splitting: " + regex);

        String[] words = originalText.split(regex);

        System.out.println("\nLEXEMES:");
        int count = 0;
        for (String word : words) {
            if (!word.isEmpty()) {
                System.out.println(word);
                count++;
            }
        }
        
        System.out.println("\nTotal: " + count);
        
        scanner.close();
    }
}