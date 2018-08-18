from easydollar.USD import usd

################################################
## add two dollar amounts ##

husband_income = usd('55000.00')

# if it's a whole dollar amount, the decimal is optional.
wife_income = usd('62000')

household_income = husband_income + wife_income

print(f'Total household income: {household_income}\n')


# USD instances will implicitly roll over cents into dollars when cast to a string.
money1 = usd('1.50')
money2 = usd('0.50')
total = money1 + money2
print (f'Dollar addition: {money1} + {money2} = {total}')

print (f"Output of usd('0.5255') = {usd('0.5255')}")
print(f"Output of usd('1000575.100') = {usd('1000575.100')}")
print()

###############################################



## make change from a transaction ##

price = usd('56.60')

paid = usd('60.00')

change = paid - price

print(f'Price: {price}')
print(f'Paid: {paid}')
print (f'Change due: {change}')
print()

##############################################



## IMPORTANT!! ##
# The multiply operator on the USD object is a "scale" operation (only accepts a whole number)
# You can't multiply two USD's together.

payrate = usd('15.00')
hours_worked = 40

paycheck = payrate * hours_worked

print(f'This weeks earnings: {paycheck}\n\n')

#############################################



## Division, and Interest Multiplication ##

# The divide operator for USD objects is a distribution function.

# Similar to the multiply operator, a USD instance can only be divided by a whole number.

# Performance note: the division will invoke USD's 'distribute' method (which returns a list of USD objects)
# and returns the first element from that list.

loan_amount = usd('10653.26')

interest = 21   # 21 percent (21%)

total_loan_interest = loan_amount.interest(interest)

term = 60

monthly_principle = loan_amount / term
monthly_interest = total_loan_interest / term

first_payment = monthly_interest + monthly_principle

print('~~ Loan Issued. ~~')
print(f'Loan Amount: {loan_amount}')
print(f'Interest: {interest}%')
print(f'Term: {term} months')
print(f'Total interest to be paid over term: {total_loan_interest}\n')

print(f'Principle monthly: {monthly_principle}')
print(f'Interest monthly: {monthly_interest}\n')
print(f'First payment due: {first_payment}')

print('\n~~ xx xx xx xx ~~\n')


#################################################

input()