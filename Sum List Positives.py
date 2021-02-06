#-------------------------
#Name: Parker Holmes
#Challenge: Write a function to sum the positive numbers in a given list.
#If the numbers are 0 or below, return 0. If the list is empty, return 0.
#Date: 02/06/2021
#-------------------------

def positive_sum(arr):
    sum = 0
    for x in arr:
        if x > 0:
            sum += x
        elif x <= 0:
            sum += 0
    return sum