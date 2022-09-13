class Employee:
    #class variables
    num_of_employees = 0
    House_officers_pay = 200000
    Registrars_pay = 300000
    Consultans_pay = 500000

    #Class atributes
    def __init__(self, first, last, email, level):
        self.first = first
        self.last = last
        self.email  = email
        self.level = int(level)
        Employee.num_of_employees += 1
        self.pay_raise = 1.05

    #Class methods(Regular methods)
    def fullName(self):
        return f'{self.first} {self.last}'
        #return '{} {}'.format(self.first, self.last) Alternative syntax

    def pay(self):
        if self.level > 0 and self.level < 4:
            if self.level == 1:
                return Employee.House_officers_pay
            elif self.level == 2:
                return Employee.Registrars_pay
            else:
                return Employee.Consultans_pay
        else:
            return 'Invalid level selection'
    
    def apply_payRaise(self):
        if self.level > 0 and self.level < 4:
            if self.level == 1:
                Employee.House_officers_pay *= self.pay_raise
            elif self.level == 2:
                Employee.Registrars_pay *= self.pay_raise
            else:
                Employee.Consultans_pay *= self.pay_raise
        else:
            return 'Invalid level selection'

    #class methods(class methods)
    @classmethod
    def reset_pay_amount(cls, HO_pay, registra_pay, consultant_pay):
        cls.House_officers_pay = HO_pay
        cls.Registrars_pay = registra_pay
        cls.Consultans_pay = consultant_pay

    #class methods as alternative constructor to accept another format
    #of input
    @classmethod
    def from_string(cls, emp_str):
        first, last, email, level = emp_str.split('-')
        return cls(first, last, email, level)

#Test instances     
emp1 = Employee('Gideon', 'Obiasor', 'gideonobiasor@gmail.com', 2)
emp2 = Employee('Sharon', 'Ezeugo', 'sharonezeugo@gmail.com', 3)
emp3 = Employee.from_string('Jason-Emma-jason@gmail.com-2')

print(Employee.num_of_employees)
print(emp1.fullName(), emp1.email, emp1.pay())
print(emp2.fullName(), emp2.email, emp2.pay())
print(emp3.fullName(), emp3.email, emp3.pay())

Employee.reset_pay_amount(400000, 600000, 800000)
print()
print(emp1.fullName(), emp1.email, emp1.pay())
print(emp2.fullName(), emp2.email, emp2.pay())
print(emp3.fullName(), emp3.email, emp3.pay())
