class Employee:
    def __init__(self, name, salary, department):
        # private attribute
        self._name = name
        self.__salary = salary
        self.__department = department

    # private method
    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {}'.format(self.__salary))
        print('แผนก = {}'.format(self.__department))

emp1 = Employee('สมศักดิ์', 50000, 'วิชาการ')
emp1.__salary = 70000
emp1.showData()