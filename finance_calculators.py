import math

# CAPSTONE PROJECT

# 1) ASK the user which financial calculator they want

choose_financial_calculator = (input("Type the name of the financial calculator that you would like to use: "))

# 2a) IF user has typed investment, convert to lower case and, ask the user the following:
# i) The amount of money that they are depositing;
# ii) The investment interest rate (as a percentage);
# iii) The number of years they plan on investing;
# iv) If they want 'simple' or 'compound' interest.

if choose_financial_calculator.lower() == "investment":
    print("You have chosen the investment calculator.")
    amount_of_money = float(input("Type the amount of money that you are depositing in Pounds Sterling: "))
    investment_interest_rate = float(input("Type your interest rate as a percentage, excluding the percentage sign: "))
    number_of_years = float(input("Type the number of years that you plan to be investing: "))
    interest = input("Do you want the calculation for simple or compound interest?: ")



# 2b) FOR investment, calculate total amount (using simple interest or compound interest, depending on which interest the user has chosen) by doing the following: 
# DEFINE percentage interest rate as investment interest rate divided by 100

# CALCULATE total amount (using simple interest) using the equation P*(1 + r*t) 
# CALCULATE total amount (using compound interest) using the equation P*math.pow((1+r),t)

# IF user has typed simple, print 'Your total amount using simple interest will be (total using simple interest)'. 
# IF user has typed compound, print 'Your total amount using compound interest will be (total using compound interest)'.

    percentage_interest_rate = (investment_interest_rate) / 100

    total_simple_interest = (amount_of_money)*(1 + ((percentage_interest_rate)*(number_of_years)))
    total_compound_interest = (amount_of_money)*math.pow((1+(percentage_interest_rate)),(number_of_years))

    if interest.lower() == "simple":
        print("Your total amount using simple interest will be " + str(total_simple_interest) + ".")
    elif interest.lower() == "compound":
        print("Your total amount using compound interest will be " + str(total_compound_interest) + ".")
    else:
        print("Error - please try again.")



# 3a) IF user has typed bond, convert to lower case and ask the user the following:
# i) The present value of the house
# ii) The bond interest rate
# iii) The number of months they plan to take to repay the bond

if choose_financial_calculator.lower() == "bond":
    print("You have chosen the bond calculator.")
    value_of_house = float(input("Type the value of your house in Pounds Sterling: "))
    bond_interest_rate = float(input("Type your interest rate as a percentage, excluding the percentage sign: "))
    number_of_months = float(input("Type the number of months that you plan to take to repay the bond: "))



# 3b) FOR bond repayment, calculate by doing the following: 
# DEFINE monthly interest rate as bond interest rate divided by 100 divided by 12
# CALCULATE repayment using the following equation: using the following equation: repayment = (i * P)/(1 - (1 + i)**(-n))
# PRINT 'You will have to repay (repayment) each month.'

    monthly_interest_rate = bond_interest_rate / 100 / 12

    repayment = (monthly_interest_rate)*(value_of_house) / (1 - (1 + (monthly_interest_rate)) ** -(number_of_months))

    print("You will have to repay " + str(repayment) + " each month.")







     
