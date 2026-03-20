class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}."
    

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Chef", "Cashier", "Manager", "Owner", "Computer"]
        return position in valid_positions
    
employee1 = Employee("SpongeBob", "Chef")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Mr. Krabs", "Manager")