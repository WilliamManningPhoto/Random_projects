import random

Slots = ["🍒", "🍋", "🔔", "⭐", "7"]
Money = 100

def slot_machine():
    global Money

    while Money > 0:
        choice = input("Press Enter to spin (£2) or type 'exit' to quit: ")

        if choice.lower() == 'exit':
            print(f"Thanks for playing! You leave with £{Money}")
            return

        # cost per spin
        Money -= 2

        result = [random.choice(Slots) for _ in range(3)]
        print(" ".join(result))

        if result[0] == result[1] == result[2]:
            print("🎉 Jackpot! You won £10!")
            Money += 10
        elif len(set(result)) == 2:
            print("👍 Two match! You won £4!")
            Money += 4
        else:
            print("❌ No win this time.")

        print(f"Balance: £{Money}\n")

    print("You ran out of money!")


slot_machine()


    