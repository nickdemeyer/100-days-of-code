from tracker_class import workouttracker
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
        elif choice == 4:
            workout.delete_workout()
        elif choice == 5:
            workout.save_workouts()
            print("exiting...")
            break
if __name__ == "__main__":
    main()