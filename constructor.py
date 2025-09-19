# Constructor
    # เป็น Method พิเศษที่จะถูกเรียกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
    # โครงสร้างของ Constructor
        # def __init__(self):
        #   pass

# destructor
     # เป็น Method พิเศษที่ตรงข้ามกับ Constructor จะถูกใช้งานเมื่อ
     # สิ้นสุดการทำงานของ Class หรือถูกทำก่อนจะสลาย object
     # ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
     # โครงสร้าง
        # def __del__(self)
        #   pass

# การสร้าง Constructor

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

    # มีหรือไม่มีก็ได้ destructor
    def __del__(self):
        print('call destructor')

emp1 = Employee('สมศักดิ์', 50000, 'การเงิน')
emp1.showData()

emp2 = Employee('ชาลิสง', 500, 'ฝ่ายขาย')
emp2.showData()

emp3 = Employee('รพีพัฒน์', 0.5, 'ขี้ข้า')
emp3.showData()

emp4 = Employee('plim', 20000, 'HR')
emp4.salary = 21000
emp4.showData()