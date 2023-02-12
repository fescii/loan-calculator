import math

what_to_calculate = input('type "n" for number of month payments,\ntype "a" for annuity monthly payment amount,\ntype "p" for loan principal')
if what_to_calculate == 'n':
    loan_principal = int(input('\nEnter the loan principal:'))
    monthly_payment = int(input('\nEnter the monthly payment:'))
    loan_interest = float(input('\nEnter the loan interest:'))
    
    i = loan_interest / (100 * 12)
    x = monthly_payment / (monthly_payment - i * loan_principal)
    base = 1 + i
    n = math.ceil(math.log(x, base))
    number_of_years = math.floor(n / 12)
    number_of_months = n%12
    plural = True if number_of_months > 1 else False
    
    if(number_of_years > 0):
        plural_year = True if number_of_years > 1 else False
        if(number_of_months == 0):
            print(f"\nIt will take {number_of_years} year{'s' * plural_year} to repay the loan")
        else:
                print(f"\nIt will take {number_of_years} year{'s' * plural_year} and {number_of_months} month{'s' * plural} to repay the loan")
    else:
        print(f"\nIt will take {number_of_years} month{'s' * plural} to repay the loan")
    
elif what_to_calculate == 'a':
    loan_principal = int(input('\nEnter the loan principal:'))
    periods = int(input('\nEnter the number of periods:'))
    loan_interest = float(input('\nEnter the loan interest:'))
    
    i = loan_interest / (100 * 12)
    # x = (monthly_payment / monthly_payment − i ∗ loan_principal)
    base = 1 + i
    n = math.pow(base,periods)
    payment = math.ceil(loan_principal * (i * n / (n-1)))
    print(f"\nYour monthly payment = {payment}!")
    
elif what_to_calculate == 'p':
    annuity_payment = float(input('Enter the annuity payment:'))
    periods = int(input('Enter the number of periods:'))
    loan_interest = float(input('\nEnter the loan interest:'))

    i = loan_interest / (100 * 12)
    # x = (monthly_payment / monthly_payment − i ∗ loan_principal)
    base = 1 + i
    n = math.pow(base,periods)
    
    new = (i * n / (n-1))
    principal = annuity_payment / new
    print(f"\nYour loan principal = {principal}!")
    # print(f'\nYour monthly payment = {payment} and the last payment = {last_payment}.')
