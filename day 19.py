loan_principle = 1000
ARP = 0.05
loan_term = 10
print("====== Loan Calculator ======")
print("$1000 over 10 years with 5% APR")
loan_increase = loan_principle
for year in range(loan_term):
    loan_increase = loan_increase * (1 + ARP)
    print()
    print("Year", year + 1, "is", round(loan_increase,2))
print("You paid",round(loan_increase,2),"in intrest over 10 years")
