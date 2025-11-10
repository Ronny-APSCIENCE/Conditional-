# This program calculates sales commission.
def main():
    # Create a variable to control the loop
    keep_going = 'y'

# Calculate a series of commissions.
    while keep_going == 'y':
        # Get a salesperson's sales and commission rate.
        sales = input('Enter the amount of sales: ')
        comm_rate = input('Enter the commission rates: ')

#Calculate the commission
        commission = sales * comm_rate

#Display the commission
        print(' The commissionn is %.2f.' % commission)

#See if the user wants to do another one
        keep_going = raw-input ('Do you want to calculate another ' +  'commission (Enter y for yes): ')

#Call the main function
main()