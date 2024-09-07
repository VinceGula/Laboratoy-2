# Initialization of employee's name, department, total deduction, gross income, net income
employee_name = ""
department = ""
total_deduction = 0
gross_income = 0
net_income = 0
pagibig_contribution = 100.00
sss_contribution = 0
philhealth_contribution = 0

# Accepting inputs for names of employee, department, rate per hour, number of working hours per day, number of days
# per week, number of weeks per month.
employee_name = str(input("Enter the name of the employee: "))
department = str(input("Enter the employee's department: "))
rate_per_hour = float(input("Enter employee's rate per hour: "))
num_hrs_per_day = int(input("Enter employee's working number of hours per day: "))
num_days_per_week = int(input("Enter employee's working days per week: "))
num_weeks_per_month = int(input("Enter employee's working weeks per month: "))

# Setting a formula for gross income
gross_income = rate_per_hour * num_days_per_week * num_weeks_per_month * num_hrs_per_day

# Setting a code that depicts the equivalent SSS contribution and philhealth Contribution from the value of the gross
# income.
if 0 <= gross_income <= 20000:
    sss_contribution = 100.00
    philhealth_contribution = 125.75
elif gross_income <= 20001:
    sss_contribution = 1200.00
    philhealth_contribution = 2200.50
elif gross_income <= 50001:
    sss_contribution = 6800.00
    philhealth_contribution = 4800.00
elif gross_income <= 75001:
    sss_contribution = 8800.00
    philhealth_contribution = 5800.00
else:
    print("Invalid Input. Please Try Again.")
    exit()

# Setting a formula for the calculation of both the total deduction and net income.
total_deduction = sss_contribution + pagibig_contribution + philhealth_contribution
net_income = gross_income - total_deduction

# Displaying the results including the name of employee's name, department, total deduction, gross income, net income.
print("Employee's Name: ", employee_name)
print("Department: ", department)
print("Total Deduction: ", round(total_deduction, 2))
print("Gross Income: ", round(gross_income, 2))
print("Net Income: ", round(net_income, 2))

# Preventing the program from closing immediately
input("Please Press Enter to Exit.")