# FnClassObject
# ฟังก์ชั่นที่ทำงานร่วมกับ class และ object

# isinstance และ dir คือฟังก์ชั่นที่ทำงานร่วมกับ class และ object
# โดยมีรายละเอียด ดังนี้
# isinstance => เช็คว่า object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
# dir => แสดง attribute และ method
# __class__ => แสดงชื่อ class และ object

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))




emp1 = Employee('สมศักดิ์', 50000, 'การเงิน')
emp2 = Employee('ชาลิสง', 500, 'ฝ่ายขาย')
emp3 = Employee('รพีพัฒน์', 0.5, 'ขี้ข้า')
emp4 = Employee('plim', 20000, 'HR')

print(isinstance(emp1,Employee)) # ตรวจสอบว่า obj ถูกสร้างจาก class ที่ตรวจสอบไหม
print(dir(emp1))
print(emp1.__class__)