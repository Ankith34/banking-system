class Shape{
    String color;
}
class Triangle extends Shape{

} 

public class inheritance {
    public static void main(String[] args){
        Triangle t1 = new Triangle();
        t1.color = "red";
        System.out.println("Color of triangle is: " + t1.color);
    }
}
//there are five types of inheritance in java: 
//1. Single Inheritance
//2. Multiple Inheritance
//3. Hierarchical Inheritance
//4. Multilevel Inheritance
//5. Hybrid Inheritance