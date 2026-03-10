import json
class workout:
    def __init__(self, date, exercise, sets, reps, weight):
        self.date = date
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.weight = weight

class WorkoutTracker:
    def __init__(self):
        self.workouts = []
        self.load_workouts()

    def save_workouts(self):
        data = []

        for w in self.workouts:
            data.append({
            "date": w.date,
            "exercise": w.exercise,
            "sets": w.sets,
            "reps": w.reps,
            "weight": w.weight
        })

        with open("workouts.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_workouts(self):
        try:
            with open("workouts.json", "r") as f:
                data = json.load(f)

                for w in data:
                    w_obj = workout(
                        w["date"],
                        w["exercise"],
                        w["sets"],
                        w["reps"],
                        w["weight"]
                    )

                    self.workouts.append(w_obj)

        except FileNotFoundError:
            self.workouts = []

    def view_workouts(self):
        if self.workouts == []:
            print("no workouts")
        else:
            for i, workout in enumerate(self.workouts):
                print(f"{i + 1}. {workout.date}: {workout.exercise} - {workout.sets} sets - {workout.reps} reps - {workout.weight} kg")

    def add_workouts(self):
        date = input("date today: ")
        exercise = input("exercise: ")
        while True:
            try:
                sets = int(input("number of sets: "))
                reps = int(input("number of reps: "))
                weight = float(input("number of weight: "))
            except ValueError:
                print("write a number, not a letter in sets/reps/Weight!")
                continue
            
            w = workout(date, exercise, sets, reps, weight)
            self.workouts.append(w)
            self.save_workouts()
            print("workout added")
            break

    def update_workouts(self):
        if self.workouts == []:
            print("no workouts")
            return
        self.view_workouts()
        user_inp1 = int(input("choose number workout to change: "))
        i = user_inp1 - 1
        user_inp2 = input("change date/exercise/sets/reps/weight? ")
        if user_inp2 == "date":
            user_inp3 = input("new date: ")
            self.workouts[i].date = user_inp3
            self.save_workouts()
            print("workout changed")
        elif user_inp2 == "exercise":
            user_inp3 = input("new exercise: ")
            self.workouts[i].exercise = user_inp3
            self.save_workouts()
            print("workout changed")
        elif user_inp2 == "sets":
            user_inp3 = int(input("new sets: "))
            self.workouts[i].sets = user_inp3
            self.save_workouts()
            print("workout changed")
        elif user_inp2 == "reps":
            user_inp3 = int(input("new reps: "))
            self.workouts[i].reps = user_inp3
            self.save_workouts()
            print("workout changed")
        elif user_inp2 == "weight":
            user_inp3 = float(input("new weight: "))
            self.workouts[i].weight = user_inp3
            self.save_workouts()
            print("workout changed")
    
    def delete_workouts(self):
        if self.workouts == []:
            print("no workouts")
            return
        self.view_workouts()
        user_inp1 = int(input("choose workout number to delete: "))
        i = user_inp1 - 1 
        self.workouts.pop(i)
        self.save_workouts()
        print("workout deleted")