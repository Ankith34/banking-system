class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def Display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)
s1 = Student("ankith",21,90)
s1.Display()