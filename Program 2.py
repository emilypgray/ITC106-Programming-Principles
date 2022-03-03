# Import modules program needs
import name
import meternumber
import read

# Define main function
def main():
    dotted_lines = ('\n-----------------------------------------------')
    print(dotted_lines)
    print('\nSuperstar Energy Australia (SEA) Billing System')

    #create customer file called customers.txt to read from
    customer_file = open('customers.txt', 'r')

    #read the first line in the file
    information = customer_file.readline()

    #set initial variables for while loops to start with
    another_customer = 1
    all_information = True
    #set first record to number 1
    customer_record = 1
    

    #set conditions for while loop to run
    while information != '' and another_customer == 1:
        print(dotted_lines)
        print('\nCustomer Data - Record (', customer_record, ')', sep='')
        print(dotted_lines)

        #split the string read from file into individual elements of a list
        #at the commas
        information = information.split(',')

        #if the list has more or less than five elements,
        #set variable all_information to False
        if len(information) != 5:
            all_information = False

        #create if loop to run if there are exactly five elements in the list            
        if all_information:
            #set customer information item to correct element
            #of the list
            last_name = information[0]
            #format names so that name variables will store first letter as uppercase
            #and remaining letters as lowercase
            last_name = last_name[0].upper() + last_name[1:].lower()
            first_name = information[1]
            first_name = first_name[0].upper() + first_name[1:].lower()
            meter_number = information[2]
            prev_read = information[3]
            #strip newline character from last element of list
            curr_read = information[4].rstrip('\n')

            #print the customer information
            print('\nLast name        : ', last_name)
            print('\nFirst name       : ', first_name)
            print('\nMeter number     : ', meter_number)
            print('\nPrevious reading : ', prev_read)
            print('\nCurrent reading  : ', curr_read)
            print('\n')

            #check that each item is valid using functions            
            last_name_valid, error1 = name.name_valid(last_name)
            first_name_valid, error2 = name.name_valid(first_name)
            meter_number_valid, error3 = meternumber.meter_valid(meter_number)
            prev_read_valid, error4 = read.read_valid(prev_read)
            curr_read_valid, error5 = read.read_valid(curr_read)
            

            #check that all items are valid
            if last_name_valid:
                if first_name_valid:
                    if meter_number_valid:
                        if prev_read_valid:
                            if curr_read_valid:
                                #check that current read is greater than or
                                #equal to previous read
                                if curr_read >= prev_read:                                
                                    #if all items valid, read next line of file
                                    #increase customer record number by 1
                                    #set variable another_customer to 1 so loop will run again to
                                    #test next line of data
                                    information = customer_file.readline()
                                    customer_record += 1
                                    another_customer = 1
                                else:
                                    another_customer = 0
                                    line = 5
                                    print(dotted_lines)
                                    print('\nInvalid record in line (', line, ')!', sep = '')
                                    print(dotted_lines)
                                    print('\nInvalid input! Current reading must be greater' +
                                                '\nthan or equal to previous read.')
                            else:                             
                                another_customer = 0
                                line = 5
                                print(dotted_lines)
                                #if error in this item, display 'invalid record with
                                #appropriate error message
                                print('\nInvalid record in line (', line, ')!', sep = '')
                                print(dotted_lines)
                                print('\n', error5)
                        else:
                            another_customer = 0
                            line = 4
                            print(dotted_lines)
                            print('\nInvalid record in line (', line, ')!', sep = '')
                            print(dotted_lines)
                            print('\n', error4)
                    else:
                        another_customer = 0
                        line = 3
                        print(dotted_lines)
                        print('\nInvalid record in line (', line, ')!', sep = '')
                        print(dotted_lines)
                        print('\n', error3)
                        
                else:
                    another_customer = 0
                    line = 2
                    print(dotted_lines)
                    print('\nInvalid record in line (', line, ')!', sep = '')
                    print(dotted_lines)
                    print('\n', error2)
                    
            else:
                another_customer = 0
                line = 1
                print(dotted_lines)
                print('\nInvalid record in line (', line, ')!', sep = '')
                print(dotted_lines)
                print('\n', error1)
                
                  
        #if there are not five elements in list, display error message and
        #terminate program
        else:
            another_customer = 0
            print('\nInvalid record. Record does not contain five' +
                  '\nfields')

    #if another_customer variable has been set to 0 during the program,
    #display end of data and terminate program            
    if another_customer != 0:        
        print('\nEnd of Customer Data')
        print(dotted_lines)
                                        
    #close customer_file
    customer_file.close()
    
#call the main function      
main()
