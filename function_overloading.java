class Student{
    String name;
    int age;
    public void info(String name){
        System.out.println("this is first method: " + this.name);

    }
    public void info(int age){
        System.out.println(this.age);

    }
    Student(String name,int age){
        this.name = name;
        this.age = age;
    }
}

public class function_overloading {
    public static void main(String[] args) {
        Student s1 = new Student("ankith",20);
        s1.info("ankith");
        s1.info(20);
    }
}
