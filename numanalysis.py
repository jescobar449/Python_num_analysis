#Name: Jose Melquiades Escobar

#Define main ():
def main():
    
    #Declare variables and initialize them
    num_counter = 0

    #Create an empty list
    user_list = []

    #Use the for loop with the range function to loop through 10 numbers.
    for num in range (10):
        num_counter = num + 1
        #Prompt the User to enter the numbers from 1- 10.
        #Ex: Enter number 1 of 10:
        user_num = float(input ('Enter number ' + str(num_counter) + ' of 10: '))   
        #Use append function to populate the  list
        user_list.append (user_num)

    #Use min, max, sum, functions to find the low , high and total
    #number of the list.
    #Ex:  low = min(number_list)
    low = min (user_list)
    high = max (user_list)
    total = sum (user_list)
    average = total / len(user_list)

    #Print Low, high , total and average numbers of the list.
    print ('')
    print ('Low: ', format(low, ',.2f'))
    print ('High: ', format(high, ',.2f'))
    print ('Total: ', format(total, ',.2f'))
    print ('Average: ', format(average, ',.2f'))

 

#End main() 
main ()
