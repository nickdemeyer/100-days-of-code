__Workout Tracker (JSON Version)__

A simple CLI Workout Tracker built with Python.
This version includes JSON file saving and loading, so workouts are stored even after closing the program.

__Features__

- View workouts

- Add workouts

- Update workouts

- Delete workouts

- Save workouts to a JSON file

- Load workouts automatically when the program starts

- Basic error handling using try/except

__What I Practiced__

In this project I practiced:

- Functions

- Lists

- Dictionaries

- CRUD operations

- JSON (json.dump and json.load)

- File handling

- Try/Except error handling

- Working with program state

- Understanding working directories

__How It Works__

- When the program starts, it tries to load workouts from data.json.

- If the file does not exist, it starts with an empty list.

- All workouts are stored as dictionaries inside a list.

- When exiting the program, all workouts are saved to data.json.

Example workout structure:

{
    "date": "2026-02-24",
    "exercise": "Bench Press",
    "sets": 4,
    "reps": 8,
    "weight": 80
}
