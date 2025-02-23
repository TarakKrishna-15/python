FILE_NAME = "employees.txt"

def compute_net_salary(salary, tax_deduction):
    return salary - (salary * (tax_deduction / 100))

def load_records():
    employees = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                emp_id, name, salary, tax_deduction, net_salary = line.strip().split(",")
                employees.append({
                    'emp_id': emp_id,
                    'name': name,
                    'salary': float(salary),
                    'tax_deduction': float(tax_deduction),
                    'net_salary': float(net_salary)
                })
    except FileNotFoundError:
        pass
    return employees

def save_records(employees):
    with open(FILE_NAME, "w") as file:
        for emp in employees:
            file.write(f"{emp['emp_id']},{emp['name']},{emp['salary']},{emp['tax_deduction']},{emp['net_salary']}\n")

def add_record(employees):
    while True:
        try:
            add_another = input("\nWant to add a record (Y/N): ").lower()
            if add_another == 'n':
                break
            if add_another != 'y':
                print("Invalid input. Please enter 'Y' or 'N'.")
                continue

            emp_id = input("\nEnter EMP-ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Salary: "))
            tax_deduction = float(input("Enter Tax Deduction (%): "))
            net_salary = compute_net_salary(salary, tax_deduction)
            
            employees.append({
                'emp_id': emp_id,
                'name': name,
                'salary': salary,
                'tax_deduction': tax_deduction,
                'net_salary': net_salary
            })

        except ValueError:
            print("Invalid input. Please enter valid data.")
    
    save_records(employees)

def display_records(employees):
    if not employees:
        print("\nNo records found.")
        return
    
    print("\nId\t\tNAME\t\tSALARY\t\tTAX DEDUCTION\t\tNET SALARY\n")
    for emp in employees:
        print(f"{emp['emp_id']}\t\t{emp['name']}\t\t{emp['salary']:.2f}\t{emp['tax_deduction']}%\t\t\t{emp['net_salary']:.2f}")

def main():
    employees = load_records()
    while True:
        print("\n1. ADD RECORD")
        print("2. DISPLAY RECORDS")
        print("3. EXIT")
        
        try:
            choice = int(input("\nENTER YOUR CHOICE...\n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            add_record(employees)
        elif choice == 2:
            display_records(employees)
        elif choice == 3:
            break
        else:
            print("\nINVALID CHOICE...")

if __name__ == "__main__":
    main()
