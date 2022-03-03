# Import modules storing functions program needs                          
import bill
import discount
import reads

# Define main function
def main():
    print('-------------------------------------------------')
    print('\nSuperstar Energy Australia (SEA) Billing System')
    print('\n------------------------------------------------')
    
# Set starting values for bill and discount totals to zero

    bills_total = 0.00
    discounts_total = 0.00
    
# Set variable calculate_again to ‘y’ so loop will run the first time
    calculate_again = 'y'

# Set conditions for while loop to run    
    while calculate_again == 'y' or calculate_again == 'Y':
        prev_read, curr_read = reads.get_meter_reads()
        
# If usage is a positive, pass the usage amount to the bill and
#discount functions as the argument to calculate these figures
        if curr_read > prev_read:
            print('\nThank you!')
            bill_amount = bill.calculate_bill(prev_read, curr_read)
                
# Add the bill and discount amount to the their respective running totals
            bills_total += bill_amount
            print('\n\n\nThe bill amount is: $', format(bill_amount, ',.2f'), \
                      sep ='')
            discount_amount = discount.calculate_discount(bill_amount)
            discounts_total += discount_amount
            print('\nEarly payment discount: $', \
                  format(discount_amount, ',.2f'), sep = '')
                
# If usage is negative, show an error message                
        else:
            print('\n\nBill amount must be positive. Please try again.')
                
        print('\n------------------------------------------------')     
        calculate_again = input('\nDo you want to calculate ' \
                                        'another bill? (y/n): ')
        print('\n------------------------------------------------')
            
# Ask the user if they want to run the program again            
    print('\n\nTotal bill amounts: $', format(bills_total, ',.2f'), sep = '')
    print('\nTotal discounts: $', format(discounts_total, ',.2f'), sep = '')
    print('\n\nGood bye.')
                
        
        
# Call main function
main()

