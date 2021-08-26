# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:45:00 2021

@author: th
"""

#PART A 
# annual_salary =float(input("Enter your annual salary:"))
# portion_saved=float(input("Enter the percent of your salary to save , asdecimal:"))
# total_cost = float(input("Enter the cost of your dream home:"))
# no_of_months=1
# current_savings=0.0
# monthly_salary=annual_salary/12
# current_savings=portion_saved*monthly_salary
# portion_down_payment=0.25*total_cost
# while current_savings < portion_down_payment:
#     current_savings += current_savings*0.04/12
#     current_savings += portion_saved*monthly_salary
#     no_of_months +=1
# print("number of months:",no_of_months)


#PART B
# annual_salary =float(input("Enter your annual salary:"))
# portion_saved=float(input("Enter the percent of your salary to save , asdecimal:"))
# total_cost = float(input("Enter the cost of your dream home:"))
# semi_annual_cost =float(input("Enter the semi-annual raise,as a decimal:"))
# no_of_months=1
# current_savings=0.0
# monthly_salary=annual_salary/12
# current_savings=portion_saved*monthly_salary
# portion_down_payment=0.25*total_cost
# while current_savings < portion_down_payment:
#     if no_of_months %6 ==0:
#        monthly_salary += monthly_salary*semi_annual_cost
#     current_savings += current_savings*0.04/12
#     current_savings += portion_saved*monthly_salary
#     no_of_months +=1
# print("number of months:",no_of_months)


#PART C
 
starting_salary =float(input("Enter your annual salary:"))
semi_annual_ralse=0.07
r=0.04
total_cost=1000000
portion_down_payment= 0.25*total_cost
current_savings=0
start=0
steps=0
end=10000
guess=(end + start)//2
while abs(current_savings - portion_down_payment)>=100:
    current_savings=0
    annual_salary =starting_salary
    rate=guess/10000
    for month in range(36):
        if month %6==0 and month >0:
            annual_salary += annual_salary*semi_annual_ralse
        monthly_salary=annual_salary/12
        current_savings += monthly_salary*rate+current_savings*r/12
    if current_savings <portion_down_payment:
        start =guess
    else:
        end=guess
    guess = (end+start)//2
    steps+=1
    if steps >15:
            break
    
if steps >15:
        print("It is not possible to pay the down payment in three years.")
else:
        print("Best savings rate:",rate)
        print("steps in bisection search:",steps)
                












