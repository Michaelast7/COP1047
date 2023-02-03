
# figure out how to compute income with dependents
# all taxpayers get charged a standard 20% on income
# a standard $10000 deduction is allowed
# number of dependents increases amount deductable ($3000 deduced for every dependent)

tax_rate = 0.2
standard_deduction = 10000
dependent_deduction = 3000

gross_income = float(input("Enter Gross Income: "))
numDependents = int(input("Enter number of dependents: "))

taxableIncome = gross_income - standard_deduction - dependent_deduction * numDependents
incomeTax = taxableIncome * tax_rate

print("The income tax is", str(incomeTax))