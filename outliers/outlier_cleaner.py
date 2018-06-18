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

    print predictions
    ### your code goes here
    for i in range(0,len(predictions)):
        error =  predictions[i]-net_worths[i]
        cleaned_data.append((ages[i], net_worths[i], abs(error)))

    cleaned_data.sort(key=lambda tup: (tup[2]))
    print cleaned_data
    print ages
    cleaned_data = cleaned_data[0:80]
    return cleaned_data
