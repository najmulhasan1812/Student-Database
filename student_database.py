class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def get_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled is True:
            print(f'{self.__name} is already enrolled')
        else:
            self.__is_enrolled = True
            print(f'{self.__name} enrolled successfully')

    def drop_student(self):
        if self.__is_enrolled != False:
            self.__is_enrolled = False
            print(f'{self.__name} dropped successfully')
        else:
            print(f'{self.__name} is already dropped')

    def view_student_info(self):
        if self.__is_enrolled:
            status = 'Enrolled'
        else:
            status = 'Not Enrolled'
        print(f'Name: {self.__name} ID: {self.__student_id}   Department: {self.__department} Status: {status}')


student1  = Student(1,  "Najmul Hasan", 'CST  ', False)
student2  = Student(2,  "Mahbub Hasan", 'CST  ', False)
student3  = Student(3,  "Efad        ", 'CST  ', False)
student4  = Student(4,  "Eaheiya Khan", 'CST  ', False)
student5  = Student(5,  "Osman       ", 'CST  ', False)
student6  = Student(6,  "Saimun Islam", 'EEE  ', False)
student7  = Student(7,  "Muntasir    ", 'EEE  ', False)
student8  = Student(8,  "Jakera thaki", 'EEE  ', False)
student9  = Student(9,  "Jarin Tasnim", 'EEE  ', False)
student10 = Student(10, "Bayzid      ", 'EEE  ', False)
student11 = Student(11, "Sabbir      ", 'Civil', False)
student12 = Student(12, "Rashed      ", 'Civil', False)
student13 = Student(13, "Mahin       ", 'Civil', False)
student14 = Student(14, "Mubin       ", 'Civil', False)
student15 = Student(15, "Hasan Imama ", 'Civil', False)


tmp = True

print('\n------------Welcome to our School------------\n')
while tmp == True:
    print('--------------------------------------------')
    print('1. View All Student')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. exit')
    print('--------------------------------------------')

    option = int(input("Enter your option: "))

    if option == 1:
        if not StudentDatabase.student_list:
            print("No student found")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif option == 2:
        s_id = int(input("Enter student ID: "))
        found = False
        for student in StudentDatabase.student_list:
            if student.get_id() == s_id:
                student.enroll_student()
                found = True
                break
        if not found:
            print("Invalid student ID")

    elif option == 3:
        s_id = int(input("Enter student ID: "))
        found = False
        for student in StudentDatabase.student_list:
            if student.get_id() == s_id:
                student.drop_student()
                found = True
                break
        if not found:
            print("Invalid student ID")

    elif option == 4:
        tmp = False
        print("Thank you!")
    else:
        print("Wrong option choosen. try again")