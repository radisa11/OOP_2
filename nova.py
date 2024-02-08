class Student():
    def __init__(self,name,address,phone,course,index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def get_info(self):
        print(f"Name: {self.name},Address: {self.address}, Phone: {self.phone},Course: {self.course}, Index Number: {self.index_number}")

student1 = Student("Radisa","51 W Oak st",2405517821,"Python",123/2)
student2 = Student("Irena","51 W Oak st",2405555454,"C#",123/10)
student3 = Student("Aleksandar","51 W Oak st",7805517821,"Java",123/23)

student1.get_info()
student2.get_info()
student3.get_info()