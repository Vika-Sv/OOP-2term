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
                    throw new InputMismatchException("It cant be empty!");
                int val = Integer.parseInt(line);
                if (val < min || val > max)
                    throw new IllegalArgumentException(
                        "Value " + val + " is out of range [" + min + ".." + max + "]");
                return val;
            } catch (NumberFormatException e) {
                System.out.println("Error: Please enter a valid integer!");
            } catch (IllegalArgumentException e) {
                System.out.println("Range Error" + e.getMessage());
            } catch (InputMismatchException e) {
                System.out.println("Error" + e.getMessage());
            }
        }
    }
 
    static double readDouble(String prompt, double min, double max) {
        while (true) {
            System.out.print(prompt);
            try {
                String line = sc.nextLine().trim();
                if (line.isEmpty())
                    throw new InputMismatchException("It cant be empty!");
                double val = Double.parseDouble(line.replace(',', '.'));
                if (val < min || val > max)
                    throw new IllegalArgumentException(
                        "Value " + val + " is out of range [" + min + ".." + max + "]");
                return val;
            } catch (NumberFormatException e) {
                System.out.println("Type Error: Please enter a valid number!");
            } catch (IllegalArgumentException e) {
                System.out.println("Range Error" + e.getMessage());
            } catch (InputMismatchException e) {
                System.out.println("Error" + e.getMessage());
            }
        }
    }
 
    static String readString(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                String val = sc.nextLine().trim();
                if (val.isEmpty())
                    throw new InputMismatchException("It cant be empty!");
                if (val.matches(".*\\d.*"))
                    throw new IllegalArgumentException("Field cannot contain digits!");
                return val;
            } catch (InputMismatchException e) {
                System.out.println("Error" + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("Format Error" + e.getMessage());
            }
        }
    }
 
    static String readAddress(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                String val = sc.nextLine().trim();
                if (val.isEmpty())
                    throw new InputMismatchException("It cant be empty!");
                if (val.length() < 5)
                    throw new IllegalArgumentException("Address is too short (min. 5 characters)!");
                return val;
            } catch (InputMismatchException e) {
                System.out.println("Error" + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("Format Error" + e.getMessage());
            }
        }
    }
 
    static String readPhone(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                String val = sc.nextLine().trim();
                if (val.isEmpty())
                    throw new InputMismatchException("It cant be empty!");
                if (!val.matches("[0-9()\\-+ ]{7,15}"))
                    throw new IllegalArgumentException(
                        "Invalid format! Use digits, +, -, (), space (7-15 characters).");
                return val;
            } catch (InputMismatchException e) {
                System.out.println("  [Error]           " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("  [Format Error]   " + e.getMessage());
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
                System.out.println("Error: ID" + id + "Already exists! Please enter a unique ID.");
            else
                return id;
        }
    }
 
 
    static void inputStudents() {
        int count = readInt("\nEnter count of Students (min. 5, max. 10): ", 5, 10);
 
        for (int i = 1; i <= count; i++) {
            System.out.println("\nStudent #" + i + " of " + count + " ");
            int id = readUniqueId("ID (4-digit, 1000-9999): ");
            String surName = readString ("Last Name: ");
            String address  = readAddress ("Address: ");
            String phoneNumber = readPhone ("Phone (e.g., 050-123-45-67): ");
            System.out.println("Enter 3 grades (0-100):");
            int[] grades = new int[3];
            for (int j = 0; j < 3; j++)
                grades[j] = readInt("Grade " + (j + 1) + ": ", 0, 100);
            System.out.println("Saved");
 
            Students.add(new Student(id, surName, address, phoneNumber, grades));
        }
    }
 
 
    static final String SEP =
        "+------+--------------------+--------------------------------+------------------+----------------+--------+";
 
    static void printTable(List<Student> list) {
        System.out.println();
        if (list.isEmpty()) {
            System.out.println(" No records found!");
            return;
        }
        System.out.println(SEP);
        System.out.printf("| %-4s | %-18s | %-30s | %-16s | %-14s | %-6s |%n", 
        "ID", "Last Name", "Address", "Phone", "Grades", "Average");
        System.out.println(SEP);
        for (Student a : list) {
            System.out.printf("| %-4d | %-18s | %-30s | %-16s | %-14s | %-6.1f |%n",
                a.getId(), a.getLastName(), a.getAddress(),
                a.getPhone(), a.getGradesString(), a.getAverageGrade());
        }
        System.out.println(SEP);
        System.out.println("Records found:" + list.size());
    }
 

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
 
 
    public static void main(String[] args) {
        inputStudents();

        System.out.println("\n All students");
        printTable(Students);

        boolean running = true;
        while (running) {
            System.out.println("\nMenu");
            System.out.println("  1 - Students with failing grades (below 60)");
            System.out.println("  2 - Students with average grade above a given value");
            System.out.println("  0 - Exit");
            System.out.print("Your choice: ");
 
            String choice = sc.nextLine().trim();
            switch (choice) {
                case "1":
                    System.out.println("\nResult");
                    printTable(getFailingStudents());
                    break;
                case "2":
                    double minAvg = readDouble(
                        "Enter minimum average grade (0-100): ", 0, 100);
                    System.out.printf("Result", minAvg);
                    printTable(getAboveAverage(minAvg));
                    break;
                case "0":
                    running = false;
                    break;
                default:
                    System.out.println("Error: wrong choice! Please enter 1, 2 or 0.");
            }
        }
        sc.close();
    }
}