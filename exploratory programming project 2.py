def listinput(my_list): #defines function that takes a list argument and counts the total amount of positive numbers in that list. If the argument is not a list, a type error is raised.
    counter = 0
    if (type(my_list) != list): # if statement that raises a type error of the argument is not a list
        raise TypeError("The argument is not a list")
    else:
        for items in range (0,len(my_list)): #This for loop and the nested loops individually count items within the given list in order to determine the total amount of positive numbers
            if(my_list[items]>0):
                counter += 1
            else:
                counter = counter
    print "------------------------------------------------------------------------------------------------------------------------------------------------------ \n\n"
    print "Amount of positive numbers in the list: " + str(counter) + "\n"
listinput([-232,2,3,-1000000,4,5,-3213,-2,5,-1])
listinput("ooooooo yeeeaaaaa")                                                                                                                                                                                                                                                                                                             
