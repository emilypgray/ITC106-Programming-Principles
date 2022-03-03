# Define bill function
def calculate_bill(previous_read, current_read):
    
# Calculate usage    
    usage = current_read - previous_read

# set low usage rate to $0.15 per kWh
    low_rate = 0.15

# if usage is between 1 and 1000 kWh, multiply low rate
#by usage to determine bill
    if 1 <= usage <= 1000:
        bill_total = usage*low_rate
    elif usage > 1000:
        
# set rate for usage above 100 kWh to $0.25 per kWh
        high_rate = 0.25

# use low rate up to 1000 kWh and high rate on
#any usage over 1000 kWh to determine bill
        bill_total = 1000*low_rate + (usage - 1000)*high_rate
    else:

# if usage between 0 and 1, no rate applicable and bill is $0.00
        bill_total = 0

# return variable to calling code        
    return bill_total


    
