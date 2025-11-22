from Expense import expense
import csv
import os

used = 0

def main():
    #menu
    fileName = "expensemanager.csv"
    budget = 200
    while True:
        query = int(input("Welcome. Select option: \n1. Add expense.\n2. View expenses.\n3. Delete expenses.\n0. Quit.\n"))
        
        #adding an expense
        if query == 1:
            myexpense = getExpense()
            #write expense to file
            update(myexpense, fileName)
            print("Item added successfully.\n")

        #viewing expenses
        elif query == 2:
            records = view(fileName)
            if records:
                print("Your monthly expenses are as follows: \n")
                for expense_record in records:  # Changed variable name to avoid shadowing expense class
                    print(expense_record)
                    
                print(f"\nYou have used ${used:.2f} so far.    Remaining from budget: ${budget-used:.2f}") 
            else:
                print("No records found:( \n")       
        elif query == 3:
            os.remove(fileName)
            print("All expenses successfully deleted.\n")

        else:
            break    


#prompts input -> creates expense object
def getExpense():
    #prompt for input
    name = input("Enter name of item: ")
    cost = float(input("Enter cost of item: $"))
    categoryList = ["food", "restaurant", "home", "electronics", "fun ", "other"]
    categoryOption = int(input("Choose a category: \n1. Food.\n2. Restaurant.\n3. Home.\n4. Electronics.\n5. Fun.\n6. Other.\n"))
    category = categoryList[categoryOption-1]

    #create expense object
    return expense(name, cost, category)

#writes expense to CSV file
def update(obj, file):
    with open(file, "a", newline="") as csvfile:
        appender = csv.writer(csvfile) #create writing csv object
        appender.writerow([obj.name, obj.cost, obj.category])  # Write as separate columns

#outputs all past expenses and calculates remaining budget
def view(file):
    global used  # Need to declare global to modify the global variable
    data = []
    total = 0
    try:
        with open(file, "r", newline="") as csvFile:
            reader = csv.reader(csvFile)  # Use csvFile (file object), not file (filename string)
            for row in reader:
                if row:  # Check if row is not empty
                    data.append(row)
                    
                    #get cost of each expense and add to total
                    total += float(row[1])  # Convert string to float
                    

        used = total
        return data
    except FileNotFoundError:
        return
    except Exception as e:
        return
    
        
        
   



if __name__ == "__main__":
    main()