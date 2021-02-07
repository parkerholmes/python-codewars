#-------------------------
#Name: Parker Holmes
#Challenge: Write a function that will abbreviate a given name.
#Date: 02/06/2021
#-------------------------

def abbrev_name(name):
    x = name.split(" ")
    x = [item.upper() for item in x]
    return x[0][0] + "." + x[1][0]
