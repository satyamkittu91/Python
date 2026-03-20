class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} works as a {self.position}."
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


my_company = Company("Under the Sea Inc.")
company2 = Company("chum bucket")

my_company.add_employee("SpongeBob", "Chef")
my_company.add_employee("Squidward", "Cashier")
my_company.add_employee("Mr. Krabs", "Manager")

company2.add_employee("Plankton", "Owner")
company2.add_employee("Karen", "Computer")

print(my_company.list_employees())
print(company2.list_employees())