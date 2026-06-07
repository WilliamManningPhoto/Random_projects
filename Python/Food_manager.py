
class Food_manager:

    def __init__(self):
        self.list = []

    def Ask_food(self):
        while True:
            food = input("Enter food (or 'done' to stop): ")
            if food == "done":
                break
            self.Food_list(food)

    def Food_list(self, item):
        self.list.append(item)

    def Print_list(self):
        print("Items:")
        for item in self.list:
            print(item)

F = Food_manager()

F.Ask_food()

F.Print_list()