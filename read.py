#define reads() function
def read_valid(read):

    #set standard error message    
    error= ('Meter read must be a positive' +
            '\nfloating-point number with a six-digit' +
            '\ninteger part and a single-digit decimal part.  ')

    #open a try statement for a float
    try:
        #test if read is greater than zero
        if float(read) > 0:
            #test if read is 8 characters in length
            if len(read) == 8:
                #test for single-digit decimal part
                if read[-2] == '.':
                    #set validity variable to True if all conditions
                    #satisfied
                    read_valid = True
                #if any conditions violated, set validity
                    #variable to False
                else:
                    read_valid = False                                                                         
            else:
                read_valid = False                            
        else:
            read_valid = False            
    except ValueError:
        read_valid = False

    #return validit variable, error message to main function   
    return read_valid, error



