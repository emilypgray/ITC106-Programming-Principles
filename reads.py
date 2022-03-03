# Define reads function
def get_meter_reads():

# Create a while loop to accept only numerical values
# Show an error message and prompt user for another
# input if text is entered

    while True:
        try:
            previous_read = float(input('\nEnter the previous reading : '))
            break
        except ValueError:
            print('\nValue must be a numerical figure. Please '\
                  'try again.')
    while True:
        try:
            current_read = float(input('\nEnter the current reading : '))
            break
        except ValueError:
            print('\nValue must be a numerical figure. Please '\
                  'try again.')
            
# Return previous and current reads to the calling code

    return previous_read, current_read
    









                  
                        
