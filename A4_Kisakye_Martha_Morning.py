#KISAKYE MARTHA JANEPHER 
#21/U/10006/EVE
#2100710006

#calulate the area and cirmuference of a circle
class circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_circumference(self):
        return 2*3.14*self.radius
    
    def calculate_area(self):
        return 3.14 * self.radius**2
c1 = circle(7)
print(c1.calculate_area())



#calculate the area and perimeter of a rectangle

#calculate and display employee bonus((15%))of  salary (Employee1:150000, employee2:230000)
#class Employee:
    #def __init__(self, salary):
        #self.salary = salary
    #def salary_calc(self):
        #bonus = 0.15*self.salary
        #print("Employee bonus is :", bonus)
        
#Employee1 = Employee(150000)
#Employee2 = Employee(230000)
#Employee1.salary_calc()
#Employee2.salary_calc()

#Assignmen Show encapsulation with employee information to give pay increamentation(salary with employee informtion to new_salary)
#eg from 850000 t0 1000000

class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
        
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def set_salary(self, new_salary):
        self.salary = new_salary
        
    def increase_salary(self, amount):
        self.salary+= amount
        
employee = Employee ("Kisakye Martha" , 850000)
    
print("Employee name:",employee.get_name())
print("Current salary:",employee.get_salary() )

#Increasing salary
new_salary = 1000000
employee.salary = new_salary
print("New salary:", employee.salary)