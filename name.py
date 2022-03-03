#define name_valid function
def name_valid(name):

    #test length of name greater than or equal to
    #one character
    if len(name) >= 1:
        #test length of name less than 20 characters
        if len(name) < 20:
            #test name is alphabetic
            if name.isalpha():
                #if all criteria satisfied, set first_name_valid
                #variable to True.
                #create empty message
                name_valid = True
                error = ''                                  
            else:
                #if any criteria violated, set validit variable
                #to False and error to appopriate message
                name_valid = False
                error = ('Name must be '+
                          'an alphabetic string.')                    
        else:
            name_valid = False
            error = ('Name must be less than 20 characters long. ')    
    else:
        name_valid = False
        error = ('Name must be at least one character long. ')


    #return first_name_valid and appropriate error message to main function
    return name_valid, error





