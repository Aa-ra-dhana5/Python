#A nested class is a class defined inside another class, mainly used for logical grouping and better organization when the inner class is tightly related to the outer class.


class University:
    
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print("University:", self.name)
    
    class Department:
        def __init__(self , dept_name):
            self.dept_name = dept_name
            
        def info(self):
            print("Department : " , self.dept_name)
        
        
u = University("GTU")
u.info()
d=University.Department("Computer")
d.info()