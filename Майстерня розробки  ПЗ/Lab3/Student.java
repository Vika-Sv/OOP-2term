public class Student{
   private int id;
    private String surName;
    private String phoneNumber;
    private String address;
    private int[] grades;


    public Student(int id, String surName, String phoneNumber, String address, int[]grades){
        this.id = id;
        this.surName = surName;
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.grades = grades;   
    }

    public int    getId()        { return id; }
    public String getLastName()  { return surName; }
    public String getAddress()   { return address; }
    public String getPhone()     { return phoneNumber; }
    public int[]  getGrades()    { return grades; }

    public double getAverageGrade() {
        int sum = 0;
        for (int g : grades) sum += g;
        return (double) sum / grades.length;
    }
 
    public boolean hasFailingGrades() {
        for (int g : grades) if (g < 60) return true;
        return false;
    }
 
    public String getGradesString() {
        return grades[0] + ", " + grades[1] + ", " + grades[2];
    }

}

