import math

# assign data
principal = 172000
boe_rate = 2.25
extra_rate = 1.49

# total rate
total_rate = (boe_rate + extra_rate) / 100

# monthly interest
interest = principal * total_rate / 12

print(interest)
#output
536.0666666666667