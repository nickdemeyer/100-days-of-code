__Workout Tracker (CLI – Dictionary Version)__
__Overview__

This is a command-line Workout Tracker built in Python.

The goal of this version was to refactor the original list-based implementation into a cleaner and more scalable structure using dictionaries. Each workout is now stored as a dictionary, making the code more readable and maintainable.

The application allows users to manage workouts directly from the terminal using a menu-based system.

__Features__

- View all workouts

- Add a new workout

- Update existing workouts

- Delete workouts

- Track workout date

- Safe handling of empty workout lists

- Structured using functions and a main controller

__Data Structure__

Workouts are stored in a list.

Each workout is represented as a dictionary:

{
    "date": "2026-02-14",
    "exercise": "Bench Press",
    "sets": 4,
    "reps": 8,
    "weight": 80
}


The full data structure looks like:

[
    {workout1},
    {workout2},
    {workout3}
]


This approach improves readability compared to index-based lists and allows easier future expansion.

__Program Structure__

The application is organized into separate functions:

- view_workout(workouts) → Displays workouts

- add_workout(workouts) → Adds a new workout

- update_workout(workouts) → Updates a selected field

- delete_workout(workouts) → Removes a workout

- main() → Controls program flow and menu system

The main() function acts as the central controller of the application.

__Concepts Practiced__

- Dictionaries

- Lists of dictionaries

- Mutable data structures

- Function parameters

- Control flow (return, break)

- Enumerate

- CRUD logic

- Clean program structure


__Purpose of This Project__

This project is part of a structured learning journey focused on mastering Python fundamentals and building toward larger end-to-end applications.

The focus of this version was improving data modeling and understanding how dictionaries enhance clarity and scalability.
