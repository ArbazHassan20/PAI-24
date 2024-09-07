def save_biodata_to_file(file_path, name, cnic, age, salary):
    try:
        with open(file_path, 'w') as file:
            file.write(name)
            file.write("\n")
            file.write(cnic)
            file.write("\n")
            file.write(age)
            file.write("\n")
            file.write(salary)
            file.write("\n")
        print("Employee biodata saved successfully to", file_path)
    except Exception as e:
        print("An error occurred while saving biodata:", e)


def append_contact_to_file(file_path, contact_number):
    try:
        with open(file_path, 'a') as file:
            file.write("Contact Number: " + contact_number + "\n")
        print("Contact number appended successfully to", file_path)
    except Exception as e:
        print("An error occurred while appending contact:", e)


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("\n--- Employee Biodata ---")
            print(content)
    except FileNotFoundError:
        print("Error: The file", file_path, "was not found.")
    except Exception as e:
        print("An error occurred while reading the file:", e)


name = input("Enter employee name: ")
cnic = input("Enter employee CNIC number: ")
age = input("Enter employee age: ")
salary = input("Enter employee salary: ")
file_path = 'biodata.txt'

save_biodata_to_file(file_path, name, cnic, age, salary)

contact_number = input("Enter employee contact number: ")
append_contact_to_file(file_path, contact_number)

read_file(file_path)
