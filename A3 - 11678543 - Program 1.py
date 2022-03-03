# Import modules program needs   
import name
import meternumber
import read



# Define main function
def main():
    print('\n-----------------------------------------------')
    print('\nSuperstar Energy Australia (SEA) Billing System')
    print('\n------------------------------------------------')

    #create customer file called customers.txt to write data to
    customer_file = open('customers.txt', 'w')

    # Set variable calculate_again to ‘y’ so loop will run the first time
    # set all information validity variables to false
    calculate_again = 'y'
    last_name_valid = False
    first_name_valid = False
    meter_number_valid = False
    prev_read_valid = False
    curr_read_valid = False

    # Set conditions for while loop to run    
    while calculate_again == 'y':

        # Set while loop to run while last name invalid
        while not last_name_valid:
            #ask user for last name
            last_name = input('\nEnter last name          : ')
            #check validity using a function
            last_name_valid, error = name.name_valid(last_name)
            #print error message if valid returns false
            if not last_name_valid:
                print('\nInvalid input!', error)

        #format valid input                
        last_name = last_name[0].upper() + last_name[1:].lower()

        #repeat same loop process for other information variables
        while not first_name_valid:
            first_name = input('\nEnter first name         : ')
            first_name_valid, error = name.name_valid(first_name)
            if not first_name_valid:
                print('\nInvalid input!', error)

        first_name = first_name[0].upper() + first_name[1:].lower()

        while not meter_number_valid:
            meter_number = input('\nEnter meter number       : ')
            meter_number_valid, error = meternumber.meter_valid(meter_number)
            if not meter_number_valid:
                print('\nInvalid input!', error)
            
        while not prev_read_valid:
            prev_read = input('\nEnter previous reading   : ')
            prev_read_valid, error = read.read_valid(prev_read)
            if not prev_read_valid:
                print('\nInvalid input!', error)

        while not curr_read_valid:
            curr_read = input('\nEnter current reading    : ')
            curr_read_valid, error = read.read_valid(curr_read)
            if not curr_read_valid:
                print('\nInvalid input!', error)
            #test if valid input for curr_read is greater than or equal
            #to prev_read
            else:             
                if float(curr_read) < float(prev_read):
                    curr_read_valid = False
                    print('\nInvalid input! Current reading must be greater' +
                          '\nthan or equal to previous read.')
            

        #create a list with customer information as elements
        customer_info = [last_name,first_name,meter_number,prev_read,curr_read]

        #duplicate list with comma as the separator between elements and newline
        #character to finish the list
        customer_info = ','.join(customer_info) + '\n'
        
        #write list to customer file
        customer_file.write(customer_info)

        
        print('\n\n-----------------------------------------------')
        #user input to run program again
        calculate_again = input('\nDo you want to enter another customer? (y/n): ')
        print('\n-----------------------------------------------')

        #set user input to lowercase
        calculate_again = calculate_again.lower()

        #set while loop so that only 'y' or 'n' accepted as answers        
        while calculate_again != 'y' and calculate_again != 'n':
            print('\nSorry, I didn\'t understand that.')
            calculate_again = input('\n\nDo you want to enter another customer? (y/n): ')
            print('\n-----------------------------------------------')
            calculate_again = calculate_again.lower()

        #reset validit variables to false so input loops will run again
        last_name_valid = False
        first_name_valid = False
        meter_number_valid = False
        prev_read_valid = False
        curr_read_valid = False
     
    #close customer file
    customer_file.close()

    print('\n\nGoodbye.')

#call the main function
main()




