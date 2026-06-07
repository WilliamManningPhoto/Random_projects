from operator import index


Items = ["Ham Sandwich", "Chocolate bar", "Sweets", "Energy drink"]
Item_prices = [12.50, 25.20, 15.00, 2.00]
Money = 20

def selection():
    choice = input("What item from the vending machine would you like to buy? (1: Ham Sandwich, 2: Chocolate bar, 3: Sweets, 4: Energy drink): ")
    if choice in ['1', '2', '3', '4']:
        item_index = int(choice) - 1
        print(f"You selected {Items[item_index]} which costs ${Item_prices[item_index]}.")
        payment(item_index)
    else:
        print("Invalid choice.")

def payment(item_index):
    global Money, Item_prices

    print(f"You have ${Money} available.")
    choice = input("Would you like to proceed with the payment? (yes/no)")

    if choice.lower() =='yes':
        print("Processing payment...")
        if Money > Item_prices[item_index]:
            Money -= Item_prices[item_index]
            print(f"Payment successful! Remaining balance: ${Money}")
        else:
            print("Insufficient funds.")
    elif choice.lower() =='no':
        print("Payment cancelled.")
    else:
        print("Payment cancelled.")
    

while True:
    selection()
