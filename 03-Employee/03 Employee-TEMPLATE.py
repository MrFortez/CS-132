#####################################################################
# author:       
# date:         
# description:  
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################



######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################


######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################


