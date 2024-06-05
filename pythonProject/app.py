import datetime
import pprint
import json





file_path = "expsenses.json"

with open(file_path, 'r') as json_file:
    expenses = json.load(json_file)
def add():
    print("add")
    expense_id = datetime.datetime.now().isoformat()
    item = input("Enter the expense item: ").strip()
    amount = float(input("Enter the amount: ").strip())
    expenses[expense_id]={"item":item,"amount":amount}
def read():
    print("read")
    pprint.pprint(expenses)

def update():
    print("update")
    pprint.pprint(expenses)
    id = input("Enter the id that you want to update").strip()
    item = input("Enter the expense item: ").strip()
    amount = float(input("Enter the amount: ").strip())

    expenses[id]["item"]=item
    expenses[id]["amount"]=amount

def delete():
    print("delete")
    pprint.pprint(expenses)
    id = input("Enter the id that you want to delete").strip()
    expenses.pop(id)
    pprint.pprint(expenses)

operations = {

    1: add,
    2: delete,
    3: update,
    4: read,
    5: exit

}

def display_options():
    print("Select an option from below")
    print("1. Add")
    print("2. Remove")
    print("3. Update")
    print("4. View")
    print("5. Exit")

def main():
    with open(file_path, 'w') as json_file:
        json.dump(expenses, json_file, indent=4)
    display_options()
    option = int(input())
    print("Your selected option is "+str(option))
    operations.get(option)()
    main()

if __name__ == '__main__':
    main()
