public class Student{
   private int id;
    private String surName;
    private int phoneNumber;
    private String adress;
    private int[] grades;


    public Student(int id, String surName, int phoneNumber, String adress, int[]grades){
        this.id = id;
        this.surName = surName;
        this.phoneNumber = phoneNumber;
        this.adress = adress;
        this.grades = grades;   
    }

    public int    getId()        { return id; }
    public String getLastName()  { return surName; }
    public String getAddress()   { return adress; }
    public int    getPhone()     { return phoneNumber; }
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

