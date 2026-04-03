import java.util.*;

public class main {
 
    static Scanner sc = new Scanner(System.in);
    static List<Student> Students = new ArrayList<>();
 
    
    static int readInt(String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            try {
                String line = sc.nextLine().trim();
                if (line.isEmpty())
                    throw new InputMismatchException("Поле не може бути порожнім!");
                int val = Integer.parseInt(line);
                if (val < min || val > max)
                    throw new IllegalArgumentException(
                        "Значення " + val + " поза діапазоном [" + min + ".." + max + "]");
                return val;
            } catch (NumberFormatException e) {
                System.out.println("  [Помилка типу]      Введіть ціле число!");
            } catch (IllegalArgumentException e) {
                System.out.println("  [Помилка діапазону] " + e.getMessage());
            } catch (InputMismatchException e) {
                System.out.println("  [Помилка]           " + e.getMessage());
            }
        }
    }
 
    static double readDouble(String prompt, double min, double max) {
        while (true) {
            System.out.print(prompt);
            try {
                String line = sc.nextLine().trim();
                if (line.isEmpty())
                    throw new InputMismatchException("Поле не може бути порожнім!");
                double val = Double.parseDouble(line.replace(',', '.'));
                if (val < min || val > max)
                    throw new IllegalArgumentException(
                        "Значення поза діапазоном [" + min + ".." + max + "]");
                return val;
            } catch (NumberFormatException e) {
                System.out.println("  [Помилка типу]      Введіть число (наприклад: 75 або 80.5)!");
            } catch (IllegalArgumentException e) {
                System.out.println("  [Помилка діапазону] " + e.getMessage());
            } catch (InputMismatchException e) {
                System.out.println("  [Помилка]           " + e.getMessage());
            }
        }
    }
 
    static String readString(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                String val = sc.nextLine().trim();
                if (val.isEmpty())
                    throw new InputMismatchException("Поле не може бути порожнім!");
                if (val.matches(".*\\d.*"))
                    throw new IllegalArgumentException("Поле не повинно містити цифри!");
                return val;
            } catch (InputMismatchException e) {
                System.out.println("  [Помилка]           " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("  [Помилка формату]   " + e.getMessage());
            }
        }
    }
 
    static String readAddress(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                String val = sc.nextLine().trim();
                if (val.isEmpty())
                    throw new InputMismatchException("Поле не може бути порожнім!");
                if (val.length() < 5)
                    throw new IllegalArgumentException("Адреса занадто коротка (мін. 5 символів)!");
                return val;
            } catch (InputMismatchException e) {
                System.out.println("  [Помилка]           " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("  [Помилка формату]   " + e.getMessage());
            }
        }
    }
 
    static String readPhone(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                String val = sc.nextLine().trim();
                if (val.isEmpty())
                    throw new InputMismatchException("Поле не може бути порожнім!");
                if (!val.matches("[0-9()\\-+ ]{7,15}"))
                    throw new IllegalArgumentException(
                        "Невірний формат! Використовуйте цифри, +, -, (), пробіл (7-15 символів).");
                return val;
            } catch (InputMismatchException e) {
                System.out.println("  [Помилка]           " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("  [Помилка формату]   " + e.getMessage());
            }
        }
    }
 
    static int readUniqueId(String prompt) {
        while (true) {
            int id = readInt(prompt, 1000, 9999);
            boolean duplicate = false;
            for (Student a : Students) {
                if (a.getId() == id) { duplicate = true; break; }
            }
            if (duplicate)
                System.out.println("  [Помилка]           ID " + id + " вже існує! Введіть інший.");
            else
                return id;
        }
    }
 
 
    static void inputStudents() {
        int count = readInt("\nСкільки абітурієнтів ввести? (мін. 5, макс. 20): ", 5, 20);
 
        for (int i = 1; i <= count; i++) {
            System.out.println("\n  ┌─── Абітурієнт #" + i + " з " + count + " ───");
            int    id       = readUniqueId("  │ ID (4-значне, 1000-9999)       : ");
            String lastName = readString  ("  │ Прізвище                       : ");
            String address  = readAddress ("  │ Адреса                         : ");
            String phone    = readPhone   ("  │ Телефон (напр. 050-123-45-67)  : ");
            System.out.println("  │ Введіть 3 оцінки (0-100):");
            int[] grades = new int[3];
            for (int j = 0; j < 3; j++)
                grades[j] = readInt("  │   Оцінка " + (j + 1) + "                      : ", 0, 100);
            System.out.println("  └─── Збережено ✓");
 
            Students.add(new Student(id, lastName, address, phone, grades));
        }
    }
 
 
    static final String SEP =
        "+------+--------------------+--------------------------------+------------------+----------------+--------+";
 
    static void printTable(List<Student> list) {
        System.out.println();
        if (list.isEmpty()) {
            System.out.println("  ╔══════════════════════════════════════════════════════╗");
            System.out.println("  ║   Даних за заданим критерієм пошуку не знайдено!     ║");
            System.out.println("  ╚══════════════════════════════════════════════════════╝");
            return;
        }
        System.out.println(SEP);
        System.out.printf("| %-4s | %-18s | %-30s | %-16s | %-14s | %-6s |%n",
            "ID", "Прізвище", "Адреса", "Телефон", "Оцінки", "Серед.");
        System.out.println(SEP);
        for (Student a : list) {
            System.out.printf("| %-4d | %-18s | %-30s | %-16s | %-14s | %-6.1f |%n",
                a.getId(), a.getLastName(), a.getAddress(),
                a.getPhone(), a.getGradesString(), a.getAverageGrade());
        }
        System.out.println(SEP);
        System.out.println("  Знайдено записів: " + list.size());
    }
 
    // =========================================================
    // МЕТОДИ ПОШУКУ
    // =========================================================
 
    static List<Student> getFailingStudents() {
        List<Student> res = new ArrayList<>();
        for (Student a : Students) if (a.hasFailingGrades()) res.add(a);
        return res;
    }
 
    static List<Student> getAboveAverage(double min) {
        List<Student> res = new ArrayList<>();
        for (Student a : Students) if (a.getAverageGrade() > min) res.add(a);
        return res;
    }
 
    // =========================================================
    // ГОЛОВНИЙ МЕТОД
    // =========================================================
 
    public static void main(String[] args) {
        System.out.println("╔══════════════════════════════════════════════════════╗");
        System.out.println("║      СИСТЕМА ОБЛІКУ АБІТУРІЄНТІВ  (Варіант 23)       ║");
        System.out.println("╚══════════════════════════════════════════════════════╝");
 
        // --- Крок 1: введення даних ---
        System.out.println("\n--- ВВЕДЕННЯ ДАНИХ ---");
        inputStudents();
 
        // --- Крок 2: вивести всіх після введення ---
        System.out.println("\n=== ВВЕДЕНІ ДАНІ (всі абітурієнти) ===");
        printTable(Students);
 
        // --- Крок 3: пошук ---
        boolean running = true;
        while (running) {
            System.out.println("\n--- ПОШУК ---");
            System.out.println("  1 - Абітурієнти з незадовільними оцінками (< 60)");
            System.out.println("  2 - Абітурієнти із середнім балом вище заданого");
            System.out.println("  0 - Вихід");
            System.out.print("Ваш вибір: ");
 
            String choice = sc.nextLine().trim();
            switch (choice) {
                case "1":
                    System.out.println("\n=== РЕЗУЛЬТАТ: абітурієнти з незадовільними оцінками ===");
                    printTable(getFailingStudents());
                    break;
                case "2":
                    double minAvg = readDouble(
                        "Введіть мінімальний середній бал (0-100): ", 0, 100);
                    System.out.printf("%n=== РЕЗУЛЬТАТ: середній бал вище %.1f ===%n", minAvg);
                    printTable(getAboveAverage(minAvg));
                    break;
                case "0":
                    System.out.println("\nДо побачення!");
                    running = false;
                    break;
                default:
                    System.out.println("  [Помилка] Введіть 0, 1 або 2!");
            }
        }
        sc.close();
    }
}