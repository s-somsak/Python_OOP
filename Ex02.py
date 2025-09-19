# เขียนโปรแกรมสร้าง class ชื่อ people โดยมี Attribute และ Method ดังนี้
# attrbute
#   name เป็นชื่อของบุคคล
#   age เป็นอายุของบุคคล
# method
#   Introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ My name is <name>. I'm <age> years old

class people():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        return print("My name is {}. I'm {} years old".format(self.name, self.age))

ppl1 = people("Somsak", 23)
ppl1.Introduce()