class workouttracker:
    def __init__(self):
        self.workouts = []
    
    def view_workouts(self):
        if self.workouts == []:
            print("no workouts")
        else:
            for i, workout in enumerate(self.workouts):
                print(f"{i + 1}. {workout["date"]}: {workout["exercise"]} - {workout["sets"]} sets - {workout["reps"]} reps - {workout["weight"]} kg")

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
        

def main():
    workout = workouttracker()

    while True:
        print("1. view workouts")
        print("2. add workout")
        print("3. update workout")
        print("4. delete workout")
        print("5. exit")
        choice = int(input("choose number 1-5: "))

        if choice == 1:
            workout.view_workouts()
        elif choice == 2:
            workout.add_workout()
        elif choice == 3:
            workout.update_workout()
        elif choice == 5:
            print("exiting...")
            break
main()