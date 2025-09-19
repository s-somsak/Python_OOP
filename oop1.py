# ชื่อ ,เงินเดือน
class Employee: # การสร้าง class
    # สร้าง Method
    def detail(self, name, salary, department):
        # สร้าง Attribute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

# Attribute เป็นกลไกที่กำหนดคูณสมบัติให้กับ class
# การสร้าง Attribute
    # self.name = ชื่อพนักงาน
    # self.salary = เงินเดือน
    # self.age = อายุของพนักงาน
# Method เป็นกลไกที่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
#   def getName(self):
#       return self.name
# การเรียกใช้งาน
#   ชื่อวัตถุ.getName()

# คีย์เวิร์ด self
#   การใช้คีย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
#   ให้บอกตัวตนของวัตถุนั้น ๆ เช่น การกำหนดคุณสมบัติต่าง ๆ ในวัตถุ

# Constructor
#   เป็น method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง Constructor
#   def __init__(self):
# การสร้างวัตถุ

emp1 = Employee()
emp1.detail('สมศักดิ์', 50000, 'การเงิน')
emp1.showData()

emp2 = Employee()
emp2.detail('ชาลิสง', 500, 'ฝ่ายขาย')

emp3 = Employee()
emp3.detail('รพีพัฒน์', 0.5, 'ขี้ข้า')