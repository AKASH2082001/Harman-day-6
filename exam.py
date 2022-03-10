class Student(object):
    def __init__(self,name,rollno,admino,college):
        self.name = name
        self.rollno = rollno
        self.admino = admino
        self.college = college

    def displaystudentdata(self):
        print(self.name)
        print(self.rollno)
        print(self.admino)
        print(self.college)

class Exam(Student):
    def __init__(self,name,rollno,admino,college,examname,engmark,matmark,phymark,chemark):
        self.examname = examname
        self.engmark = engmark
        self.matmark = matmark
        self.phymark = phymark
        self.chemark = chemark

        Student.__init__(self,name,rollno, admino, college)

    def printexamdetails(self):
        print("name :",self.name)
        print("rollno :",self.rollno)
        print("admino :",self.admino)
        print("college :",self.college)
        print("exam name :",self.examname)
        print("english mark :",self.engmark)
        print("maths mark :",self.matmark)
        print("physics mark :",self.phymark)
        print("chemistry mark :",self.chemark)

student1 = Exam("AKASH","1","201","ACE","SEMESTER 2","90","98","78","76")

student1.printexamdetails()
y = Student("ram","3","90","ace")

y.displaystudentdata()
