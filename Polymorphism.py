#Polymorphism
# การพ้องรูป
# เกิดจาก poly หลากหลาย morphology รูปแบบ
# ในทางโปรแกรมคือการ method ชื่อเดียวกัน สามารถรับอาร์กิวเมนต์ที่แตกต่างกัได้หลายรูปแบบ
# โดย method นี้จะถูกเรียกว่า overload method

class Employee:
    #class variable
    _minSalary = 30000
    maxSalary = 50000
    companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        # Prive attribute
        self.__name = name
        self.__salary = salary
        self._department = department


    # Prive method
    def _showData(self):
        print('ชื่อพนักงาน = ' + self.__name)
        print('เงินเดือน  = ', format(self.__salary))
        print('แผนก  = ' + self._department)

        #รายได้ต่อปี
    def _grtIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}"
                .format(self.__name, self._department, self.__salary, self._grtIncome()))

class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.age = age

    def _showData(self):
        super()._showData()
        print("อายุ = " + str(self.age))

class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self, name, salary, experiece, skill):
        super().__init__(name, salary, self.__departmentName)
        self.experiece = experiece
        self.skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = " + str(self.experiece) + "ปี")
        print("ทักษะ = " + str(self.skill))

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = " + str(self.area))

account = Accounting("นูน", 30000,25)
account._showData()

programmer = Programmer("โน๊ต", 60000,2,"พัฒนาเกม")
programmer._showData()

sale = Sale("นัด", 25000, "เชียงคาน")
sale._showData()