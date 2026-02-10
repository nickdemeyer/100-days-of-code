🏋️ Simple Workout Tracker (CLI)

A simple command-line application written in Python to manage workouts and exercises.

🎯 Project Goal

This project was built to practice:

Nested lists

Menu-based programs

Handling user input

Index-based updates

Debugging logical mistakes

🧠 Concepts Used

while True loop

if / elif / else

Lists & nested lists

enumerate()

Index calculation (user_input - 1)

CRUD logic (Create, Read, Update, Delete)

⚙️ Features
1️⃣ View Workouts

Displays all stored workouts in the format:

1. Squats - 3 sets - 12 reps


Shows a message if no workouts exist.

2️⃣ Add Exercise

Asks for three inputs:

Exercise name

Number of sets

Number of reps

Stores the data correctly as:

[name, sets, reps]

3️⃣ Update Exercise

Select an exercise by number

Choose whether to update sets or reps

Updates the selected value using list indexing

4️⃣ Delete Exercise

Select exercise by number

Removes it using .pop(index)

5️⃣ Exit

Closes the program safely.

🐛 Bug & Fix
❌ Problem

In option 2 (add exercise), I initially tried to use a for loop.

This caused issues because:

The inputs were different, not repetitive

A loop was unnecessary and confusing

✅ Solution

Collect inputs directly and store them as a single nested list:

workouts.append([user_inp1, user_inp2, user_inp3])


➡️ Cleaner structure
➡️ Simpler logic
➡️ Fewer bugs
