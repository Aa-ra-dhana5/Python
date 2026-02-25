#Single Tasking using Thread

from threading import Thread

class MyExam:
    def solve_ques(self):
        self.q1()
        self.q2()
        self.q3()
    
    def q1(self):
        print("Question 1 is solved")
    def q2(self):
        print("Question 2 is solved")
    def q3(self):
        print("Question 3 is solved")
        
myexam = MyExam()
t = Thread(target=myexam.solve_ques())
t.start()