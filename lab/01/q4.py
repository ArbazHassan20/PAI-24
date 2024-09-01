def employee(name, salary=1000):
    salary_after_tax = salary * 0.98  # Deduct 2% tax
    print("Name:", name)
    print("Salary after tax:", salary_after_tax)

# Examples of calling the function
employee("nob")
employee("med", 8000)
