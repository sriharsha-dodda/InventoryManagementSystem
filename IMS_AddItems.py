import json

#print("adding")
# read TheInventory.json(r) into dict
# close it
inventoryFile = open("TheInventory.json", "r")
inventoryDictionary = json.load(inventoryFile)
inventoryFile.close()

print("Enter your choice:")
print("1.Add new Item\n2.Add stock to existing item")
choice = int(input())
if choice == 1:
    # read details of new item
    #     name
    #     weight
    #     stock
    #     original cost
    #     discount
    print("Enter details of new item to be added:")
    newItemName = input("Enter new item name: ")
    newItemQuantity = input("Enter new item quantity: ")
    newItemStock = input("Enter new item stock: ")
    newItemOCost = input("Enter new item original cost: ")
    newItemDiscount = input("Enter new item discount: ")
    newItemPrice = str( int(newItemOCost) - int(newItemDiscount))
    newItemList = [newItemName, newItemQuantity, newItemStock, newItemOCost, newItemDiscount, newItemPrice]

    # get id of last item
    keysList=[]
    keysList = inventoryDictionary.keys()
    lastID = max(keysList)
    newItemID = int(lastID)+1

    # save the item as new item into dict
    inventoryDictionary[newItemID] = newItemList

    # open TheInventory.json(w)
    # write the new data(dict) to the file
    # close it!
    inventoryFile = open("TheInventory.json", "w")
    inventoryDictionaryString = json.dumps(inventoryDictionary, indent=1)
    inventoryFile.write(inventoryDictionaryString)
    inventoryFile.close()
    print("Item Added successfully!!")
elif choice == 2:
    invalidID = True
    while(invalidID):
        print("Enter details of existing item to be added:")
        exItemID = input("Enter item ID: ")
        if exItemID in inventoryDictionary.keys():
            invalidID = False
        elif exItemID == -1:
            exit()
        else:
            print("The ID doesn't exixts. Please correct ID! or enter -1 to exit.")
    #while end

    addedStock = input("Enter added stock quantity: ")

    # save the item as new item into dict
    inventoryDictionary[exItemID][2] = str(int(inventoryDictionary[exItemID][2]) + int(addedStock))

    # open TheInventory.json(w)
    # write the new data(dict) to the file
    # close it!
    inventoryFile = open("TheInventory.json", "w")
    inventoryDictionaryString = json.dumps(inventoryDictionary, indent=1)
    inventoryFile.write(inventoryDictionaryString)
    inventoryFile.close()
    print("Stock Added Successfully!!")
