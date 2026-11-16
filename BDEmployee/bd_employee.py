employee_name = input("Enter the Employee's name: ").title().strip()
employee_position = input("Enter the job title: ").title().strip()
employee_department = input("Enter the department: ").title().strip()
employee_salary = float(input("Enter the employee's salary: "))

print(30 * "=")
print("Employee Information".center(30))
print(30 * "=")
print()
print(f"Name: {employee_name}")
print(f"Position: {employee_position}")
print(f"Department: {employee_department}")
print(f"Salary: R$ {employee_salary:.2f}")
print()

if employee_salary > 4000:
    print(f"Salary classification: R$ {employee_salary:.2f} | Faixa C")
elif employee_salary >= 2000:
    print(f"Salary classification: R$ {employee_salary:.2f} | Faixa B")
else:
    print(f"Salary classification: R$ {employee_salary:.2f} | Faixa A")

print(30 * "=")