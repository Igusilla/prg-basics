# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.height = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.height = 183
    student2.name = "Olivia"
    student2.age = 21
    student2.height = 162
    student3.name = "Adam"
    student3.age = 20
    student3.height = 198

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.height} cm height')
    print(f'{student2.name}, {student2.age} years old, {student2.height} cm height')
    print(f'{student3.name}, {student3.age} years old, {student3.height} cm height')

if __name__ == "__main__":
    main()