import First
import Second

First.name()
Second.name()

# if not specified then last imported is priotrized

school = First.MySchool()
school.disp()

class1 = First.MyClass()
class1.show()

college = Second.MyCollege()
college.name()