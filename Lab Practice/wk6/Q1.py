##############
# Question 1 #
##############
# demonstrate classes and objects
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@rockets.utoledo.edu"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
        

emp1 = Employee("Harry", "Potter", 50000)
emp2 = Employee("Dobby", "Elf", 70000)

print(f"{emp1.email}\n{emp2.email}")

print(f"{emp1.fullname()}\n{emp2.fullname()}")