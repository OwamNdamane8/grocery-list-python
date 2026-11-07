"""
groceryList = [ "apples", "bananas", "milk", "bread"]
for x in groceryList:
    print(x)
"""

groceryList = []
name = "stop"

userItem = input("Type in an item (or 'stop' to finish): ").strip().lower()
while userItem != name:
    if userItem == "":
        print("You didn't type anything. Try again.")
    elif userItem in groceryList:
        print(userItem + " is already on your list.")
    else:
        groceryList.append(userItem)
        print(userItem + " added.")

    userItem = input("Type in an item (or 'stop' to finish): ").strip().lower()

# Show the final list
if len(groceryList) == 0:
    print("Your list is empty.")
else:
    print("\nYour grocery list:")
    for number, item in enumerate(groceryList, start=1):
        print(str(number) + ". " + item)
    print("Total items:", len(groceryList))

print("Thank you for using our app")
    
##print("List: ", groceryList)

"""
groceryList = []
for x in range(4):
    userItem = input("Type in an item: ")
    groceryList.append(userItem)
print("List: ", groceryList)\
"""
"""
grocery_list = ["apples", "bananas", "milk", "bread"]
print("Grocery List:")
for item in grocery_list:
    print(item)
    """