hours_worked = float(input("Enter the number of hours worked: "))
hourly_wages = float(input("Enter the hourly wages: "))

if hours_worked <= 40:
    total_wages = hours_worked * hourly_wages
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 1.5 * hourly_wages
    total_wages = 40 * hourly_wages + overtime_pay

print("Total wages earned: $", round(total_wages, 2))
