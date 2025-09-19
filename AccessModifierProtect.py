class Employee:
    def __init__(self, name, salary, department):
        # protected attribute
        self._name = name
        self._salary = salary
        self._department = department

    # protected method
    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {}'.format(self._salary))
        print('แผนก = {}'.format(self._department))

emp1 = Employee('สมศักดิ์', 50000, 'วิชาการ')
emp1.salary = 51000
emp1.showData()