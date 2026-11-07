groceryList = []
name = "stop"

# Allows user to type in item
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
    
grocery_list = ["apples", "bananas", "milk", "bread"]
print("Grocery List:")
for item in grocery_list:
    print(item)
    """
