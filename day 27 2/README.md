# 🏋️ Workout Tracker – Project Structure Upgrade (Day 27)

Today I improved the structure of my Workout Tracker project by learning how to work with **multiple files and modules** in Python.

## 🚀 What I Worked On

Instead of keeping everything in one file, I separated the project into:

- `main.py` → contains the dashboard / menu logic
- `tracker_class.py` → contains the `workouttracker` class and its methods

This makes the project cleaner, easier to maintain, and more professional.

---

## 📂 New Project Structure
workout_tracker/
│
├── main.py
└── tracker_class.py

## 🧠 What I Learned Today

### 1️⃣ How Python Modules Work

A `.py` file is a module.

To use a class from another file:

```python
from tracker_class import workouttracker

Now I can create an object in main.py:
workout = workouttracker()

I also learned the difference between:
import tracker_class
vs
from tracker_class import workouttracker

2️⃣ __The Purpose of__ if __name__ == "__main__":
if __name__ == "__main__":
    main()
This ensures that:
- main() only runs when the file is executed directly
- Not when it’s imported as a module
This is an important concept for writing modular Python applications.

3️⃣ __Thinking in Structure__

Today wasn’t about adding features.

It was about:
-Organizing code
-Understanding responsibility separation
-Preparing the project for scaling
This is how real-world applications are structured.

