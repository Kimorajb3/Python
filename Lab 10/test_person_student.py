#importing student and person class
from student import Student
from person import Person

#Person object
Pers = Person('Steven', 'Christopher', 'Rainbow Rd', 'Galaxy', '20374')

#print full name and address
Pers.get_full_name()
Pers.get_full_address()

#Student object
Stu = Student('Pete', 'Cat', 'Fier St', 'Pennysworth', '56932', 2022, 'Accounting')

#print Student full name, gradinfo, and greet them
Stu.get_full_name()
Stu.gradinfo()
Stu.greeting()
