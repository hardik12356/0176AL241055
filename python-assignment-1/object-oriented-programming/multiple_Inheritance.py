class Teacher:
    def teach(self):
        print("Professor teaches students")

class Researcher:
    def research(self):
        print("Professor does research")

class Professor(Teacher, Researcher):
    def work(self):
        print("Professor performs both tasks")

obj = Professor()
obj.teach()
obj.research()
obj.work()