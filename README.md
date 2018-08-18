# easydollar | py
###### written by Sean Franklin (sean.patrick516@gmail.com)

```
pip install easydollar
```

Floating-Points should **never** be used in money calculations!

This module contains the **USD** data-type, which can replace clunky "BigInt" interfaces for handling and representing cash without using *any* floating-point values or arithmetic.

The intuitive nature of this class will become obvious as you incorporate it in your existing projects.
*For example,*
If you're getting the cash amount data from user input or from reading a file, you can just wrap the **str** with *usd()*
```python
amount = usd(input('Enter cash amount $'))
```


**Note**
"Instantiating a **USD** with a **float**" is a feature intentionally left out. Input like 50.20 actually becomes *50.2* which then becomes *$50.02*
..which is obviously incorrect.



## How to use the USD type

**Note**
You can see the output of all the below examples by writing
```python
import easydollar.examples
```

#### How to import
It is recommended you use the **lower-case** *usd()*
to instantiate USD instances.

*usd()* casts a **str** to a **USD** instance.

```python
from easydollar.USD import usd
```

#### Add cash amounts

*Example 1*
```python
husband_income = usd('55000.00')

# if it's a whole dollar amount, the decimal-point is optional.
wife_income = usd('62000')

household_income = husband_income + wife_income

print(f'Total household income: {household_income}\n')
```

*Example 2*
```python
# USD instances will implicitly roll over cents into dollars when cast to a string.
money1 = usd('1.50')
money2 = usd('0.50')
total = money1 + money2
print (f'Dollar addition: {money1} + {money2} = {total}')

print (f"Output of usd('0.5255') = {usd('0.5255')}") # Outputs "$52.55"
print(f"Output of usd('1000575.100') = {usd('1000575.100')}") # Outputs "$1,000,576.00"
```


#### Making change from a transaction

```python
price = usd('56.60')

paid = usd('60.00')

change = paid - price

print(f'Price: {price}')
print(f'Paid: {paid}')
print (f'Change due: {change}')
```


## IMPORTANT!
The multiply operator on the USD object is a "scale" operation (only accepts a whole number)
*You can't multiply two USD's together.*

```python
payrate = usd('15.00')
hours_worked = 40

paycheck = payrate * hours_worked

print(f'This weeks earnings: {paycheck}')
```


#### Division, and Interest Multiplication 

The divide operator in **USD** is a *distribution* function.

Similar to the *multiply* operator, a USD instance can only be "divided" by a whole number.

## IMPORTANT!
The division operator is not a *true division* (this would involve using floating-point values in some cases.) Instead, it invokes USD's 'distribute' method.

*USD.distribute(n)* distributes the *USD*-instance's value among *n* and returns a **list** of **USD**

If you were to sum the elements of the list, you would have
the pre-*distribute()* value **exactly**

The divide "/" operator is **only** a shorthand for *my_usd.distribute(n)[0]*

## IMPORTANT!
If you add the result of the "/" operator *n* times, you **might not**
get the original value.

```python
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
```

Using the division operator here is okay, because this is a calculation of the first payment.
It is equivilent to 
```python
monthly_principle = loan_amount.distribute(term)[0]
```

To find the current payment, you could do:
```python
current_payment = my_usd.distribute(total_term)[payments_already_made]
```
or
```python
current_payment = my_usd.distribute(remaining_term)[0]
```

*A feature to streamline this is being worked on.*


## Other features of note:

#### with_interest(percent)
```python
appreciated_value = my_usd.with_interest(50) # 50% appreciation
```

#### apply_interest(percent)
```python
my_usd.apply_interest(0.6) # Applies 0.6% interest to my_usd
```