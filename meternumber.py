#define meter_number() function
def meter_valid(meter_number):

    try:
        meter_number = int(meter_number)    
            #check length of number is correct
        if len(str(meter_number)) == 8:
                #check number is in correct range
            if (int(meter_number) >= 26000000) and (int(meter_number) <= 79999999):
                #if all criteria satisfied, set meter_valid variable to 0
                meter_valid = True
                error = ''
            #if any other criteria not satifsfied, set meter_valid
            #variable to False and display appropriate
            #error message
            else:
                meter_valid = False
                error = ('Meter number is outside valid range.' +
                         '\nMeter number must be between 26000000'
                         '\nand 79999999')                
        else:
            meter_valid = False
            error = ('Meter number must be 8 digits long.')
            
    except ValueError:
        meter_valid = False
        error = ('Meter number must be an integer.')
            

    #return meter number to main fucntion
    return meter_valid, error
            




