# การสืบทอดคุณสมบัติ (inheritance)

# หลักการของ inheritance คือ ทำการสร้างสิ่งใหม่ขึ้นด้วยการสืบทอดหรือรับเอา (inheritance)
# คุณสมบัติบางอย่างมาจากสิ่งเดิมที่มีอยู่แล้วโดยการสร้างเพิ่มเติมจากสิ่งที่มีอยู่แล้วได้เลย

# ข้อดีของการ inheritance คือการที่สามารถนำสิ่งที่เคยสร้างขึ้นแล้วนำกลับมาใช้ใหม่ (re - use) ได้
# ทำให้ช่วยประหยัดเวลาในการทำงานลง เนื่องจากไม่ต้องเสียเวลาพัฒนาใหม่ทั้งหมด

# Class -> ยกเว้น Private Attribute & Private Method

# การสืบทอดคุณสมบัติ
# คลาสแม่
# class Employee:

# คลาสลูก
# class Programmer(Employee)

class Employee:
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        #instance variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = {}'+ self.__name)
        print('เงินเดือน = {}'+ self.__salary)
        print('แผนก = {}'+ self.__department)

class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self):
        pass

class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self):
        pass

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self):
        pass

    def getName(self):
        return self.__name

account = Accounting()
print(account._companyName)

programmer = Programmer()
print(programmer._minSalary)

sale = Sale()
print(sale._maxSalary)