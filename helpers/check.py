from mongoConnection import *

def check_exists(query,collection):
    '''
    Given a query, checks if a particular document exists in a particular collection

    Takes: query with the attributes to check
    Returns: True or False 
    '''
    res = read_coll(collection,query)
    if len(res) > 0:
        return True
    else:
        return False

def check_params(kwargs, obligatory, at_least_one=None):
    '''
    Given a query, checks if the query contains the required attributes for a particular function

    Takes: query to be executed
    Returns: true or false
    '''
    for param in obligatory:
        if param not in kwargs.keys():
            return False
    if at_least_one:
        contains = 0
        for param in at_least_one:
            if param in kwargs.keys():
                contains +=1
        if contains == 0:
            return False
    return True 