class Job:
    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def talk(self):
        print(f"{self.name} earns {self.salary} while working {self.hours_worked} hours a week")

class Doctor(Job):
    def __init__(self, experience, specialty):
        super().__init__("Doctor", "$70,000", 48)
        self.experience = experience
        self.specialty = specialty

class Teacher(Job):
    def __init__(self, subject, position):
        super().__init__("Teacher", "$50,000", 53)
        self.subject = subject
        self.position = position

class Lawyer(Job):
    def __init__(self, field, firm):
        super().__init__("Lawyer", "$80,000", 60)
        self.field = field
        self.firm = firm

# Creating instances
doc = Doctor("7 years", "Paediatric Consultant")
teach = Teacher("Computer Science", "Teacher")
law = Lawyer("Corporate Law", "Smith & Associates")

# Calling the talk method
doc.talk()
teach.talk()
law.talk()
