class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20  # 20% bonus for managers

    def hire(self):
        return f"{self.name} is hiring someone."


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus for developers

    def write_code(self):
        return f"{self.name} is writing code."


class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.30  # 30% bonus for senior managers


# Example usage
manager = Manager("Rao", 80000)
developer = Developer("Muratza", 60000)
senior_manager = SeniorManager("Mohammad", 100000)

# Calculating bonuses
print(f"{manager.name}'s bonus: ${manager.calculate_bonus():.2f}")
print(f"{developer.name}'s bonus: ${developer.calculate_bonus():.2f}")
print(f"{senior_manager.name}'s bonus: ${senior_manager.calculate_bonus():.2f}")

# Calling specific methods
print(manager.hire())
print(developer.write_code())
