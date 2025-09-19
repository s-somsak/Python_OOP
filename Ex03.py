# เขียนโปรแกรมสร้าง class ชื่อ Humen โดยมี Attribute และ Method ดังนี้
# attrbute
#   name เป็นชื่อของบุคคล
#   age เป็นอายุของบุคคล
# method
#   aging(year) รับ parameter 1 ตัว คือ year
#       - แสดงอายุปัจจุบัน
#       - เพิ่มอายุเท่ากับ year
#       - แสดงอายุหลังจากเพิ่มแล้ว

class Humen():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self, year):
        print("ชื่อ {} ปัจจุบันอายุ {} ปี".format(self.name, self.age))
        self.age += year
        return print("อีก {} ปีผ่านไปจะอายุ {} ปี".format( year, self.age))

ppl1 = Humen("นิว", 23)
ppl1.aging(6)