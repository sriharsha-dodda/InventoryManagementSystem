import json

def buyItem():
    '''funtion to buy item'''

    # read TheInventory.json(r) into dict
    # close it!
    #print("buying")
    billString = ""
    totalAmount=0
    totalSavings=0
    transactionItemIDList=[]
    transactionItemQuantityList=[]

    inventoryFile = open("TheInventory.json", "r")
    inventoryDictionary = json.load(inventoryFile)
    inventoryFile.close()

    # read id, quantity of each item using 
    # looped choice
    while(True):
        print(" 1.Add Item to bill\n 2.End Bill")
        buyChoice = int(input())
        if(buyChoice == 1):
            # read data: id, quantity
            # check loop if quantity<=stock:
            #     if no, then 
            #     choice:
            #         1-re-enter the quantity
            #         2-remove item
            #             break
            invalidID=True
            invalidQuantity=True

            while(invalidID):
                userInputID = input("Enter item ID:")
                if userInputID in inventoryDictionary:
                    invalidID=False
                else:
                    print("Enter valid ID")
            
            while(invalidQuantity):
                userInputQuantity = int(input("Enter item Quantity:"))
                if userInputQuantity <= int(inventoryDictionary[userInputID][2]):
                    invalidQuantity=False
                else:
                    print("Quantity exceeds stock!!")
                    print("Please enter value less then or equal to "+inventoryDictionary[userInputID][2])
            
            itemStockQuantity = int(inventoryDictionary[userInputID][2])
            itemName = inventoryDictionary[userInputID][0]
            if(len(itemName)<20):
                itemName=itemName+str(" "*int(20-len(itemName)))
            elif len(itemName)>=20:
                itemName = itemName[:18]+"*"
            itemDiscount = int(inventoryDictionary[userInputID][4])*userInputQuantity
            itemOriginalPrice = int(inventoryDictionary[userInputID][3])*userInputQuantity
            itemPrice = itemOriginalPrice - itemDiscount

            #adding ID, quantity to transaction data
            transactionItemIDList.append(userInputID)
            transactionItemQuantityList.append(userInputQuantity)

            #Reduce the purchased quantity from inventory
            inventoryDictionary[userInputID][2] = str(itemStockQuantity - userInputQuantity)
            
            #Updating Inventory
            inventoryFile = open("TheInventory.json", "w")
            inventoryDictionaryString = json.dumps(inventoryDictionary, indent=1)
            inventoryFile.write(inventoryDictionaryString)
            inventoryFile.close()

            # add string to bill
            itemBillString = str(userInputID)+"\t"+str(itemName)+"\t"+str(userInputQuantity)+"\tRs."+str(itemDiscount)+"\tRs."+str(itemOriginalPrice)
            billString += "\n"+itemBillString

            #Adding to final values
            totalAmount += itemPrice
            totalSavings += itemDiscount

            print("*"*55)
            print("* Item added:")
            print("* Name:"+str(itemName))
            print("* Quantity: "+str(userInputQuantity))
            print("* Item Amount: Rs."+str(itemPrice))
            print("* Present Total: Rs."+str(totalAmount))
            print("*"*55)
            
        elif buyChoice == 2:
            invalidPhoneNumber = True
            while(invalidPhoneNumber):
                customerPhoneNumber = int(input("Please Enter your Phone Number:"))
                if(len(str(customerPhoneNumber)) !=10):
                    print("Invalid Number!!")
                else:
                    invalidPhoneNumber = False
            break
    #end while loop

    #opening sales.json
    salesFile = open("sales.json", "r")
    salesDictionary = json.load(salesFile)
    salesFile.close()

    #getting Transaction id
    newTransactionID = len(salesDictionary)+1

    #making new transaction dictionary
    newTransactionDictionary = {"amt":totalAmount, "pids":transactionItemIDList, "quants":transactionItemQuantityList, "savs":totalSavings,"phno":customerPhoneNumber}

    #adding it to sales.json
    salesDictionary[newTransactionID] = newTransactionDictionary

    #updating sales file
    salesFile = open("sales.json", "w")
    salesDictionaryString = json.dumps(salesDictionary, indent=1)
    salesFile.write(str(salesDictionaryString))
    salesFile.close()

    print("*"*55)
    print(("*"*20)+"ABCD SuperMart"+("*"*21))
    print(("*"*17)+"visit ABCDstore.com !"+("*"*17))
    print("TransactionID: "+str(newTransactionID))
    print("Phone Number: "+str(customerPhoneNumber))
    
    print("ItemID\tName\t\t  Quantity    Discount    MRP")
    print(billString)
    print("*"*55)
    print("Total Amount: Rs."+str(totalAmount))
    print("Total Savings: Rs."+str(totalSavings))
    print("*"*55)
    print("******Thank You For Purchasing At ABCD SuperMart*******")
    print(("*"*19)+"Have a great day!"+("*"*19))
    print("*"*55)


if __name__ == "__main__":
    exitStatus=0
    print("*"*15+"Welcome to ABCD SuperMart"+"*"*15)
    print("Please Enter Your Choice")

    buyItem()
