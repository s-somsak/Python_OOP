# AccessModifier
# คือระดับในการเข้าถึง class attribute method และอื่น ๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิ์ในการเข้าใช้งาน หารซ้อนข้อมูล และอื่น ๆ

# Public คือ การประกาศระดับการเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวได้ว่าใคร ๆ ก็สามารถเข้าถึงและเรียกใช้งานได้

# Protected(_) เป็นการประกาศระดับการเข้าถึงเฉพาะ Class ของตัวมันเองและ class ลูกที่สืบทอดคุณสมบัติ

# Private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของ
# ตัวมันเองเท่านั้นที่มีสิทธิ์ใช้งานได้

class Employee:
    def __init__(self, name, salary, department):
        # Public Attribute
        self.name = name
        self.salary = salary
        self.department = department

    # Public Method
    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

emp1 = Employee('สมศักดิ์', 50000, 'การเงิน')
emp1.salary = 51000
emp1.showData()
emp2 = Employee('ชาลิสง', 500, 'ฝ่ายขาย')
emp3 = Employee('รพีพัฒน์', 0.5, 'ขี้ข้า')
emp4 = Employee('plim', 20000, 'HR')