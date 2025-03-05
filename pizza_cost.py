#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 4, 2025
# This program asks the user for the diameter
# of the pizza. it then calculates and displays
# the total cost of the pizza with tax
import constants 

def main ():
    # get the diameter from the user
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # calculate the total with tax
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax 

    #display the total with tax
    print("")
    print("The total cost is ${:,.2f}".format(total))

if __name__ == "__main__":
    main()
