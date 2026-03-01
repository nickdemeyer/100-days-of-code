# 🏋️ Workout Tracker (OOP + JSON)

A simple CLI-based Workout Tracker built with Python using Object-Oriented Programming (OOP) principles and JSON for data persistence.

## 🚀 Project Overview

This project allows users to:

- View workouts
- Add workouts
- Update workouts
- Delete workouts
- Automatically save data to a JSON file
- Automatically load data when the program starts

The goal of this project was to better understand:

- Classes and methods
- `__init__` constructor
- Instance attributes (`self`)
- JSON loading and saving
- Error handling with `try` / `except`
- Reusing methods inside a class
- Building a simple CLI dashboard with a loop

---

## 🧠 What I Learned

### 1️⃣ Structuring an OOP Project
Instead of writing everything as separate functions, I created a `WorkoutTracker` class that:

- Stores workouts in `self.workouts`
- Handles loading and saving data
- Contains all CRUD methods

This made the program cleaner and more organized.

---

### 2️⃣ JSON Persistence
On startup:
- The app tries to load `data.json`
- If the file does not exist, it starts with an empty list

On exit:
- The workouts list is saved back to `data.json`

This makes the data persistent between sessions.

---

### 3️⃣ Debugging Lessons

Some key bugs I fixed:

- ❌ Accidentally calling a list like a function in `json.dump(self.workouts(f))`
- ❌ Breaking f-strings by using double quotes inside double quotes
- ❌ Forgetting to assign loaded JSON data to `self.workouts`

Fixing these helped me better understand:
- How Python reads functions vs variables
- How string formatting works
- How data flows inside a class

---

## 🛠 Tech Used

- Python
- JSON
- Object-Oriented Programming (OOP)
- CLI (Command Line Interface)

---

## 📌 Future Improvements

- Add input validation
- Improve error handling
- Refactor update method
- Possibly convert workouts into their own class
- Add sorting or filtering features

---

## 💪 Day 26 of Learning Python

This project was challenging, especially understanding how classes interact with data.  
But pushing through confusion helped me understand OOP on a deeper level.
