class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        self.tax_percentage = 2.0 
    
    def get_data(self):
        self.name = input("Enter the employee name: ")
        self.salary = float(input("Enter salary: "))
        self.tax_percentage = float(input("Enter percentage of tax: "))
    
    def Salary_after_tax(self):
        tax_amount = (self.tax_percentage / 100) * self.salary
        salary_after_tax = self.salary - tax_amount
        return salary_after_tax
    
    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage
        print(f"Tax percentage updated to {self.tax_percentage}%")
        new_salary_after_tax = self.Salary_after_tax()
        print(f"New salary after tax: {new_salary_after_tax:.2f}")

if __name__ == "__main__":
    emp = Employee()
    emp.get_data()
    print(f"Salary after tax: {emp.Salary_after_tax():.2f}")
    new_tax = float(input("Enter new tax percentage: "))
    emp.update_tax_percentage(new_tax)
