# Fitness Tracker CLI (Day 28)

A simple **Command Line Interface (CLI) Fitness Tracker** built with Python.
This project allows users to track **workouts and meals**, store them in **JSON files**, and manage them through a menu system.

This project was created as part of my **Python learning journey (Day 28)** to practice:

* Object-Oriented Programming (OOP)
* File handling
* JSON data persistence
* CLI menu systems

---

# Features

### Workout Tracking

* Add workouts
* View all workouts
* Update existing workouts
* Delete workouts

Each workout stores:

* Date
* Exercise name
* Sets
* Reps
* Weight

### Meal Tracking

* Add meals
* View meals
* Update meals
* Delete meals

Meals are also stored and managed through the CLI menu.

### Data Persistence

All data is saved using **JSON files**, so your workouts and meals are stored even after closing the program.

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

* **main.py** → Handles the CLI menu and program flow
* **workout_class.py** → Workout and WorkoutTracker classes
* **meal_class.py** → Meal and MealTracker classes
* **JSON files** → Store persistent data

---

# Technologies Used

* Python
* Object-Oriented Programming
* JSON file storage
* Command Line Interface (CLI)

---

# What I Practiced

This project helped me practice:

* Designing **Python classes**
* Working with **lists of objects**
* Converting objects to **JSON serializable data**
* Building **CRUD operations**
* Creating **nested CLI menus**
* Handling file loading and saving
