class Person(object):
    def __init__(self,name,aadhar,phone):
        self.name = name
        self.aadhar = aadhar
        self.phone = phone


    def displaydetails(self):
        print(self.name)
        print(self.aadhar)
        print(self.phone)

class Employee(Person):
    def __init__(self,name,aadhar,phone,salary,designation):
        self.salary= salary
        self.designation = designation

        Person.__init__(self,name,aadhar,phone)

    def printdetails(self):
        print("Name: ",self.name)
        print("aadhar: ",self.aadhar)
        print("phone: ",self.phone)
        print("salary: ",self.salary)
        print("designation: ",self.designation)

x = Employee("akash","1234 1234 1234","0987654327","20000","manager")
x.printdetails()

y = Person("ragu", " 1243 123 1341", "90869496005")

y.displaydetails()

