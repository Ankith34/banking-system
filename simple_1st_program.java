
class Student{
    String name;
    int age;
    public void info(){
        System.out.println(this.name);
        System.out.println(this.age);
    }
}
public class simple_1st_program {
    public static void main(String[] args){
        Student s1 = new Student();
        s1.name = "ankith";
        s1.age = 20;
        s1.info();

    }

}
