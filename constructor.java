
class Student{
    String name;
    int age;
    
    Student(String name, int age){
        this.name = name;
        this.age = age;
        
    }
    public void info(){
        System.out.println(this.name);
        System.out.println(this.age);
    }
}
public class constructor {
    public static void main(String[] args){
        Student s1 = new Student("aman", 24);
        s1.info();

    }

}
