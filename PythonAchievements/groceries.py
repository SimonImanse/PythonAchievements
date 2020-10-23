
GrocerieList = ["Milk", "Eggs", "Sugar", "Coffee", "Chips", "Bread", "Butter"]
ShoppingCart = ["Coffee", "Chips", "Eggs"]
done = "(check)"
for y in ShoppingCart:
    for x in GrocerieList:
        if x == y:
            i = GrocerieList.index(x)
            GrocerieList[i] = x+done
            print(*GrocerieList)
