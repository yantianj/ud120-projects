#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    import numpy as np
    ### your code goes here
    errors = abs(predictions - net_worths)
    data_length = len(errors)/10
    # print data_length
    for num in range(1,data_length):
	where_max = np.where(errors==np.max(errors))
	errors = np.delete(errors, where_max[0])
        ages = np.delete(ages, where_max[0])
	net_worths = np.delete(net_worths, where_max[0])
        cleaned_data = zip(ages, net_worths,errors)
    return cleaned_data

