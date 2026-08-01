import json


def main():
    Exit = False

    Expenses = load()

    while(Exit == False):
        print("\nPersonal Expense Tracker ")
        print("\n1. Add New Expenses \n2. View all expenses \n3. View all expenses for a particular date \n4. View all expenses by category \n5. Calculate total expenses \n6. View Summary of expenses \n7. Delete an expenses \n8. Save the expenses in file record \n9. Exit")
        choice = int(input("Enter your choice:"))

        if(choice == 1):
            Expenses.append(NewExpenses())
        
        elif(choice == 2):
            View(Expenses)
        
        elif(choice == 3):
            ViewDate(Expenses)
        
        elif(choice == 4):
            ViewCat(Expenses)
        
        elif(choice == 5):
            Calctotal(Expenses)
        
        elif(choice == 6):
            Summary(Expenses)
        
        elif(choice == 7):
            exp = delet(Expenses)
        
        elif(choice == 8):
            save(Expenses)
        
        elif(choice == 9):
            Exit = True
        
        else:
            print("Invalid choice ")
        

    


def NewExpenses():
    date = input("Enter the date (DD-MM-YYYY):")
    while True:
        try:
            amount = float(input("Enter the amount :"))
            break
        except ValueError:
            print("Invalid Entry")
    print("Choose your category ")
    print("1. Food \n2.Transport \n3.Shopping \n4.Education \n5.Entertainment \n6.Bills \n7.Healthcare \n8.Other")
    cat = input("Enter the Category :")
    des = input("Enter the description :")

    return {'date': date , 'amount': amount , 'category' : cat , 'description' : des}


def View(exp):
    print(f"{'Date':<15}{'Amount':<12}{'Category':<15}{'Description'}")

    for i in exp:
        print(f"{i['date']:<15}{i['amount']:<12.2f}{i['category']:<15}{i['description']}")

def ViewDate(exp):
    dat = input("Enter the date (DD-MM-YYYY) :")
    print("Date       Amount      Category      Description")
    for i in exp:
        if(i["date"] == dat):
            print(f"{i['date']} {i['amount']}  {i['category']}  {i['description']}")
        

def ViewCat(exp):
    categ = input("Enter the Category :")
    print("Date       Amount      Category      Description")
    for i in exp:
        if(i["category"] == categ):
            print(f"{i['date']} {i['amount']}  {i['category']}  {i['description']}")


def Calctotal(exp):
    total = 0
    for i in exp:

        total = total + i["amount"]

    print(f"Total Expense will be {total}")

def Summary(exp):
    food = 0
    shop = 0
    trans = 0
    edu = 0
    entertain = 0

    for i in exp:
        if(i["category"] == "food"):
            food = food + i["amount"]

    for i in exp:
            if(i["category"] == "shopping"):
                shop = shop + i["amount"]

    for i in exp:
            if(i["category"] == "transport"):
                trans = trans + i["amount"]

    for i in exp:
            if(i["category"] == "education"):
                edu = edu + i["amount"]

    for i in exp:
            if(i["category"] == "entertainment"):
                entertain = entertain + i["amount"]

    


def delet(exp):
    date = input("Enter the date (DD-MM-YYYY) :")
    categor = input("Enter the category :")
    found = False
    for index,i in enumerate(exp):
        if(i["date"] == date and i["category"] == categor):
            del exp[index]
            found = True
            break

    if not found:
        print("No such expense found")

    return exp

def load():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save(exp):
    with open("expenses.json", "w") as file:
        json.dump(exp, file, indent=4)


main()