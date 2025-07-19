import csv

def calculate_emi(principal, annual_rate, months):
    monthly_rate = annual_rate / (12 * 100)
    emi = (principal * monthly_rate * ((1 + monthly_rate) ** months)) / (((1 + monthly_rate) ** months) - 1)
    return round(emi, 2)

def generate_schedule(principal, annual_rate, months):
    monthly_rate = annual_rate / (12 * 100)
    emi = calculate_emi(principal, annual_rate, months)
    schedule = []

    for month in range(1, months + 1):
        interest = round(principal * monthly_rate, 2)
        principal_component = round(emi - interest, 2)
        closing_balance = round(principal - principal_component, 2)

        schedule.append({
            'Month': month,
            'Opening Balance': round(principal, 2),
            'EMI': emi,
            'Interest': interest,
            'Principal': principal_component,
            'Closing Balance': closing_balance
        })

        principal = closing_balance

    return schedule

def save_to_csv(schedule, filename="loan_schedule.csv"):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Month', 'Opening Balance', 'EMI', 'Interest', 'Principal', 'Closing Balance']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in schedule:
            writer.writerow(entry)
    print(f"Schedule saved to {filename}")

def main():
    print("=== Diminishing Interest Loan Calculator ===")
    try:
        principal = float(input("Enter loan amount: "))
        annual_rate = float(input("Enter annual interest rate (in %): "))
        months = int(input("Enter loan tenure in months: "))

        schedule = generate_schedule(principal, annual_rate, months)
        save_to_csv(schedule)

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()

