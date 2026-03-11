# Fitness Tracker CLI (Python) — Day 29

A **Command Line Interface (CLI) Fitness Tracker** built in Python as part of my **100 Days of Code journey**.

This project allows users to **track workouts and meals**, store them in **JSON files**, and manage everything through an interactive CLI menu.

The main focus of this project was improving my understanding of:

* Object-Oriented Programming (OOP)
* JSON data persistence
* CLI application structure
* Error handling and input validation
* Working with multiple Python modules

---

# Features

## Workout Tracking

Users can:

* View workouts
* Add workouts
* Update workouts
* Delete workouts

Each workout contains:

* Date
* Exercise
* Sets
* Reps
* Weight

---

## Meal Tracking

Users can also track meals with:

* Date
* Food name
* Amount
* Calories
* Protein
* Carbs
* Fats

Just like workouts, meals support:

* View
* Add
* Update
* Delete

---

# Data Persistence

The application saves data using **JSON files**, which means:

* Workouts are saved in `workouts.json`
* Meals are saved in `meals.json`

When the program starts, the trackers load the saved data and convert it back into Python objects.

---

# Error Handling (Main Focus of This Project)

Before building this project, I practiced **basic error handling exercises**.

After that, I applied the same concepts throughout the fitness tracker so the application **does not crash when users enter incorrect input**.

Examples include:

* Catching `ValueError` when users enter letters instead of numbers
* Validating menu choices
* Ensuring the selected item exists before updating or deleting
* Using loops to ask for valid input instead of terminating the program

The goal was to make the CLI **robust and smooth to use**, even with incorrect input.

---

# Project Structure

```
project/
│
├── main.py
├── workout_class.py
├── meal_class.py
│
├── workouts.json
└── meals.json
```

### main.py

Handles:

* The main CLI menu
* Navigation between workout and meal trackers

### workout_class.py

Contains:

* `Workout` class
* `WorkoutTracker` class
* JSON loading/saving
* CRUD operations for workouts

### meal_class.py

Contains:

* `Meal` class
* `MealTracker` class
* JSON loading/saving
* CRUD operations for meals

---

# Technologies Used

* Python
* Object-Oriented Programming
* JSON file handling
* Command Line Interface
* Error handling (`try / except`)

---

# What I Learned

Through this project I practiced:

* Designing classes and objects
* Managing lists of objects
* Converting objects to JSON-compatible data
* Loading data from JSON back into objects
* Structuring a multi-file Python project
* Building nested CLI menus
* Implementing defensive programming with error handling

