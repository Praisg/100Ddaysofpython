# This program simulates a single transaction -
# either a deposit or a withdrawal - at a bank.

age = int(input("Age: "))
born_in_us = input("Born in the U.S.? (Yes/No): ")
years_of_residency = int(input("Years of Residency: "))

not_eligible_reasons = []

if age < 35:
    not_eligible_reasons.append("You are too young. You must be at least 35 years old.")
if born_in_us != "Yes":
    not_eligible_reasons.append("You must be born in the U.S. to run for president.")
if years_of_residency < 14:
    not_eligible_reasons.append("You have not been a resident for long enough. You must have at least 14 years of residency.")

if not_eligible_reasons:
    print("You are not eligible to run for president.")
    for reason in not_eligible_reasons:
        print(reason)
else:
    print("You are eligible to run for president!")
