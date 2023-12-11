# import the math library to do some caculations for this project

import math

#display the definitions of 'investment' and 'bond' to the user using print() function
#to prepare the user for the calculation they want to do.

print('''
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
''')

#ask the user to input 'investment' or 'bond' to do corresponding calculations
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# if the input doesn't match the words 'investment', 'Investment', INVESTMENT or 'bond' 'Bond', 'BOND',
# display the message that the input is invalid and prompt the user to try again.

if option not in ["investment", "Investment", "INVESTMENT", "bond", "Bond", "BOND"]:
    print("Invalid input. Try again.")

# if the input is 'investment', 'Investment' or 'INVESTMENT'

elif option in ["investment","Investment","INVESTMENT"]:
    
# ask input from the user concerning the amount of deposit,
# covert it to floats for future calculations.

    deposit = float(input("Please enter the amount you want to deposit in pounds "))
    
#as the interest rate entered is without percentage, covert it to a float
#the float is divided by 100 to get the actural the interest rate
    
    interest_rate = float(input("Please enter the number of the interest rate, without % "))/100
# ask input on the number of years the user plans on investing and convert it into a float

    years = float(input("Please enter the number of years you plan on investing "))

#ask the user to choose simple interest or compound interest
# using the list() method that include items "simple", "Simple", "SIMPLE", "compound", "Compound", "COMPOUND"
    interest = input("Do you want 'simple' or 'compound' interest? ")

#if the input doesn't match one of the four items,
# ask the user to input again. 
        
    if interest not in ["simple", "Simple", "SIMPLE", "compound", "Compound", "COMPOUND"]:
        print("Invalid entry. Type in one word.")
#if the input is the item "simple", "Simple"  or "SIMPLE" of the list,
    elif interest in ["simple", "Simple", "SIMPLE"]:
# use the formular for simple interest calculation,
# which can be expressed as, 𝐴 = 𝑃(1 + 𝑟 × 𝑡)
# where ‘r’ is the interest entered above divided by 100,
#‘P’ is the amount that the user deposits.
#‘t’ is the number of years that the money is being invested.
#‘A’ is the total amount once the interest has been applied.

        total_inv_simple = deposit * (1+interest_rate*years)
#print the final amount
        print("The final amount is", round(total_inv_simple,2), "pounds.")


# if the input is "compound", "Compound" or "COMPOUND"

    else:
#use the formular for the compound interest calculation
#𝐴 = 𝑃(1 + 𝑟)𝑡

        total_inv_compound = deposit*math.pow((1+interest_rate), years)

#print out the result
        print("The maturity value is", round(total_inv_compound, 2),"pounds.")


# if the user input 'bond', 'Bond' or "BOND"
else:

# ask input from the user on information on the value of the house,
# and convert the result that is the form of a string into a float.

    value = float(input("What's the present value of the house(in pounds)? "))

# ask input from the user on the annual interest rate
# and convert it into a float and divided by 100 for a percentage 
# and by 12 to get the monthly interest rate.

    monthly_interest_rate = float(input("Please enter the interest rate, without % "))/100/12

# the number of months to repay the loan and convert it into an int
    month = int(input("Please enter the number of months you plan to repay the loan "))

# caculate the monthly repayment using the formula 
# repayment = (i * P)/(1 - (1 + i)**(-n))

    monthly_loan = (monthly_interest_rate * value)/(1-(1+monthly_interest_rate)**(-month))

# print out the amount of the monthly loan
    print("Your monthly repayment is", round(monthly_loan, 2), "pounds each month.")

            
