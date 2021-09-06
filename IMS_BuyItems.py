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
        print("1.Add Item to bill\n2.End Bill")
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
            itemBillString = str(userInputID)+"\t"+str(itemName)+"\t"+str(itemDiscount)+"\t"+str(itemOriginalPrice)
            billString += "\n"+itemBillString

            #Adding to final values
            totalAmount += itemPrice
            totalSavings += itemDiscount

            print("Item added to bill")
        elif buyChoice == 2:
            customerPhoneNumber = int(input("Please Enter your Phone Number:"))
            break
    #end while loop

    #opening sales.json
    salesFile = open("sales.json", "r")
    salesDictionary = json.load(salesFile)
    salesFile.close()

    #getting Transaction id
    newTransactionID = len(salesDictionary)+1

    #making new transaction string
    newTransactionDictionary = {"amt":totalAmount, "pids":transactionItemIDList, "quants":transactionItemQuantityList, "savs":totalSavings,"phno":customerPhoneNumber}

    #adding it to sales.json
    salesDictionary[newTransactionID] = newTransactionDictionary

    #updating sales file
    salesFile = open("sales.json", "w")
    salesDictionaryString = json.dumps(salesDictionary, indent=1)
    salesFile.write(str(salesDictionaryString))
    salesFile.close()

    print("TransactionID: "+str(newTransactionID))
    print("ItemID\tName\t\tDiscount\tMRP")
    print(billString)
    print("*"*50)
    print("Total Amount: "+str(totalAmount))
    print("Total Savings: "+str(totalSavings))
    print("*"*50)


if __name__ == "__main__":
    exitStatus=0
    print("*"*10+"Welcome"+"*"*10)

    buyItem()


