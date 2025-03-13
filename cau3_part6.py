class Person:
    def __init__(self, name, age):
     
        self.name = name
        self.age = age

    def display_info(self):
      
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person): 
    def __init__(self, name, age, student_id):
      
        Person.__init__(self, name, age)  
       
        self.student_id = student_id

    def study(self):
      
        print(self.name, "is studying")


student = Student("Huy", 20, "12345")


student.display_info()  
student.study() 