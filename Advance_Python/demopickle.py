import pickle 

class Student:
    def __init__(self, name , role, add):
        self.name = name
        self.roll =role
        self.add =add
    
    def disp(self):
        print(f'NAme: {self.name} roll :{self.roll} Address: {self.add}')
        
with open('piklestudent.txt', mode='wb') as f:
    stu1 = Student('Rahul', 101 , 'Ranchi')
    stu2 = Student('Ramwsh', 102 , 'Shihor')
    pickle.dump(stu1, f)
    pickle.dump(stu2, f)
    print('pickling done!')

with open('piklestudent.txt', mode='rb') as f1:
    obj =pickle.load(f1)
    obj2 =pickle.load(f1)
    print('unpickling donee')
    obj.disp()
    obj2.disp()
    
    
    


    
