"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Set Variables ##
def In_State_Total():
    return 30792

def Out_of_State_Total():
    return 47882

## Interest Rate is 5% or .05 ##
## Find how much money you would recieve yearly with a 5% return on investment ##
def needed_in_state():
    return In_State_Total() / (.05)

def needed_out_state():
    return Out_of_State_Total() / (.05)

#Print both results ##
print(f"Needed_Investment_In-State = ${needed_in_state():.2f} USD")
print(f"Needed_Investment_Out-State = ${needed_out_state():.2f} USD")



in_state_gift = 615840.00
out_state_gift = 957640.00 
