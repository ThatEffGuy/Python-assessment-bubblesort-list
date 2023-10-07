#Python Assessment 2 Craig Ferguson A0112586

import os
import string

#Global Variables
#prices set to test bubblesort
itemName = []
itemPrice = []


def clear():
    os.system("cls")
    return
#end clear screen

#Prints list of items
def listItems():
    print("--------------------------------------------------")
    print("A list of your items with prices")

    i = 0
    for i in range(len(itemName)):
        print(itemName[i], "has a price of £", itemPrice[i])
        #End for

        clear()

#Gets user input to put items and prices in list. Doubtful if price over 1000000.
def inputItems():
    print("--------------------------------------------------")
    print("Please enter the details of your items:")
    item = input("Enter item name here: ")
    price = float(input("Enter the price of the item here: "))
    if price in range (0,1000000):
            itemName.append(item)
            itemPrice.append(price)
    else:
         print("That is not a vaild input")
         
         
#sort items from lowest to highest(WIP TODO - need to sort names as well as price)
def bubbleSort(itemPrice):
    
    hasSwapped = True
    numIterations = 0
    while (hasSwapped):
        hasSwapped = False
        for i in range(len(itemPrice) - numIterations - 1):
            if itemPrice[i] > itemPrice [i+1]:
                #swap
                itemPrice[i], itemPrice[i+1] = itemPrice[i + 1], itemPrice[i]
                itemName[i], itemName[i+1] = itemName[i+1], itemName[i]
                hasSwapped = True
        numIterations += 1

#total cost
def findTotalCost():
    print(sum(itemPrice))


#Purchasing with discount
def purchase():
    print("--------------------------------------------------")
    print("Finalising your purchase")
    print()
    print("Congratulations you get the cheapest item free in our special discount")
    print()
    discount = min(itemPrice)
    print("your discount has been applied")
    print()
    total = sum(itemPrice)
    fullTotal = total - discount
    print("your discount is -£", discount)
    print("your new total is £", fullTotal)
    print()


#Menu
def menu():
    print("--------------------------------------------------")
    print("Enter number for menu: ")
    print("1 = add item(s) & price(s)")
    print("2 = Sort and list items")
    print("3 = display total cost of items")
    print("4 = Display results and purchase items")
    print("5 = exit")

choice = 0
while choice != 5:

    clear()
    menu()
    choice = int(input("Enter your numerical choice: "))
    if choice == 1:
        inputItems()
    elif choice == 2:
        bubbleSort(itemPrice)
        listItems()
    elif choice == 3:
        findTotalCost()
    elif choice == 4:
        purchase()
        listItems()
    elif choice == 5:
        print("Exiting")
        break
    else:
         print ("Not an integer! Try again.")


