import json
class workouttracker:
    def __init__(self):
        self.workouts = []
        self.load_workouts()

    def load_workouts(self):
        try:
            with open("data2.json", "r") as f:
                self.workouts = json.load(f)
                print(self.workouts)
        except FileNotFoundError:
            self.workouts = []
    
    def save_workouts(self):
        with open("data2.json", "w") as f:
            json.dump(self.workouts, f)

    def view_workouts(self):
        if self.workouts == []:
            print("no workouts")
        else:
            for i, workout in enumerate(self.workouts):
                print(f'{i + 1}. {workout["date"]}: {workout["exercise"]} - {workout["sets"]} sets - {workout["reps"]} reps - {workout["weight"]} kg')

    def add_workout(self):
        user_inp1 = input("date: ")
        user_inp2 = input("exercise: ")
        user_inp3 = int(input("number of sets: "))
        user_inp4 = int(input("number of reps: "))
        user_inp5 = float(input("number of weight: "))
        workout = {"date": user_inp1, "exercise": user_inp2, "sets": user_inp3, "reps": user_inp4, "weight": user_inp5} 
        self.workouts.append(workout)
        print("workout added")
    
    def update_workout(self):
        if self.workouts == []:
            print("no workouts")
            return
        self.view_workouts()
        user_inp1 = int(input("choose number workout to change: "))
        i = user_inp1 - 1 
        user_inp2 = input("change date/exercise/sets/reps/weight?")
        if user_inp2 == "date":
            user_inp3 = input("new date: ")
            self.workouts[i]["date"] = user_inp3
            print("change confirmed")
        elif user_inp2 == "exercise":
            user_inp3 = input("new exercise: ")
            self.workouts[i]["exercise"] = user_inp3
            print("change confirmed")
        elif user_inp2 == "sets":
            user_inp3 = int(input("new sets: "))
            self.workouts[i]["sets"] = user_inp3
            print("change confirmed")
        elif user_inp2 == "reps":
            user_inp3 = int(input("new reps: "))
            self.workouts[i]["reps"] = user_inp3
            print("change confirmed")
        elif user_inp2 == "weight":
            user_inp3 = float(input("new weight: "))
            self.workouts[i]["weight"] = user_inp3
            print("change confirmed")

    def delete_workout(self):
        if self.workouts == []:
            print("no workouts")
            return
        self.view_workouts()
        user_inp1 = int(input("select workout number to delete: "))
        i = user_inp1 - 1
        self.workouts.pop(i)
        print("workout deleted")