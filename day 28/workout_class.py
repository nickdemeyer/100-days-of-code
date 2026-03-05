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

    def view_workouts(self):
        if self.workouts == []:
            print("no workouts")
        else:
            for i, workout in enumerate(self.workouts):
                print(f"{i + 1}. {workout.date}: {workout.exercise} - {workout.sets} sets - {workout.reps} reps - {workout.weight} kg")

    def add_workouts(self):
        date = input("date today: ")
        exercise = input("exercise: ")
        sets = int(input("number of sets: "))
        reps = int(input("number of reps: "))
        weight = float(input("number of weight: "))
        w = workout(date, exercise, sets, reps, weight)
        self.workouts.append(w)
        print("workout added")

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