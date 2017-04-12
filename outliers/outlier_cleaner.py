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
    x=0
    for x in range(0, len(ages)):
        new= ages[x], net_worths[x], abs(predictions[x]-net_worths[x])
        cleaned_data.append(tuple(new))
        x += 1
        cleaned_data.sort(key=lambda tup: tup[2])
    ### your code goes here

    
    return cleaned_data[:81]

