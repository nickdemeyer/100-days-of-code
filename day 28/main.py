import workout_class
import meal_class

def main():
    track_workout = workout_class.WorkoutTracker()
    track_meal = meal_class.MealTracker()

    while True:
        print("1. track workouts")
        print("2. track meals")
        print("3. exit")
        choice = int(input("choose number what you want to do: "))

        if choice == 1:
            while True:
                print("1. view workouts")
                print("2. add workouts")
                print("3. update workouts")
                print("4. delete workouts")
                print("5. go back homescreen")
                choice = int(input("choose number 1-5: "))

                if choice == 1:
                    track_workout.view_workouts()
                elif choice == 2:
                    track_workout.add_workouts()
                elif choice == 3:
                    track_workout.update_workouts()
                elif choice == 4:
                    track_workout.delete_workouts()
                elif choice == 5:
                    break
        elif choice == 2:
            while True:
                print("1. view meals")
                print("2. add meals")
                print("3. update meals")
                print("4. delete meals")
                print("5. go back homescreen")
                choice = int(input("choose number 1-5: "))

                if choice == 1:
                    track_meal.view_meals()
                elif choice == 2:
                    track_meal.add_meals()
                elif choice == 3:
                    track_meal.update_meals()
                elif choice == 4:
                    track_meal.delete_meals()
                elif choice == 5:
                    break
        
        elif choice == 3:
            print("exiting...")
            break
if __name__ == "__main__":
    main()