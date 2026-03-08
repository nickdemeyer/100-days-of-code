import json
class Meal:
    def __init__(self, date, name, amount, calories, protein, carbs, fats):
        self.date = date
        self.name = name
        self.amount = amount
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats

class MealTracker:
    def __init__(self):
        self.meals = []
        self.load_meals()

    def load_meals(self):
        try:
            with open("meals.json", "r") as f:
                data = json.load(f)

                for w in data:
                    m_obj = Meal(
                        w["date"],
                        w["name"],
                        w["amount"],
                        w["calories"],
                        w["protein"],
                        w["carbs"],
                        w["fats"]
                    )

                    self.meals.append(m_obj)

        except FileNotFoundError:
            self.meals = []

    def save_meals(self):
        data = []

        for w in self.meals:
            data.append({
            "date": w.date,
            "name": w.name,
            "amount": w.amount,
            "calories": w.calories,
            "protein": w.protein,
            "carbs": w.carbs, 
            "fats": w.fats
        })

        with open("meals.json", "w") as f:
            json.dump(data, f, indent=4)


    def view_meals(self):
        if self.meals == []:
            print("no meals")
        else:
            for i, meal in enumerate(self.meals):
                print(f"{i + 1}. {meal.date}: {meal.name} - {meal.amount} - {meal.calories} kcal - {meal.protein} g - {meal.carbs} g - {meal.fats} g")

    def add_meals(self):
        date = input("date: ")
        name = input("foodname: ")
        amount = input("amount of weight with g/ml: ")
        calories = int(input("amount of calories: "))
        protein = int(input("protein: "))
        carbs = int(input("carbs: "))
        fats = int(input("fats: "))
        m = Meal(date, name, amount, calories, protein, carbs, fats)
        self.meals.append(m)
        self.save_meals()
        print("meal added")

    def update_meals(self):
        if self.meals == []:
            print("no workouts")
            return
        self.view_meals()
        user_inp1 = int(input("choose workout number to update: "))
        i = user_inp1 - 1
        user_inp2 = input("what change? choose: date/name/amount/calories/protein/carbs/fats: ")
        if user_inp2 == "date":
            user_inp3 = input("new date: ")
            self.meals[i].date = user_inp3
            self.save_meals()
            print("meal updated")
        elif user_inp2 == "name":
            user_inp3 = input("new name: ")
            self.meals[i].name = user_inp3
            self.save_meals()
            print("meal updated")
        elif user_inp2 == "amount":
            user_inp3 = input("new amount: ")
            self.meals[i].amount = user_inp3
            self.save_meals()
            print("meal updated")
        elif user_inp2 == "calories":
            user_inp3 = int(input("new calories: "))
            self.meals[i].calories = user_inp3
            self.save_meals()
            print("meal updated")
        elif user_inp2 == "protein":
            user_inp3 = int(input("new protein: "))
            self.meals[i].protein = user_inp3
            self.save_meals()
            print("meal updated")
        elif user_inp2 == "fats":
            user_inp3 = int(input("new fats: "))
            self.meals[i].fats = user_inp3
            self.save_meals()
            print("meal updated")
    
    def delete_meals(self):
        if self.meals == []:
            print("no workouts")
            return
        self.view_meals()
        user_inp1 = int(input("choose meal number to delete: "))
        i = user_inp1 - 1
        self.meals.pop(i)
        self.save_meals()
        print("meal deleted")
