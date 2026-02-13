Workout Tracker (CLI Version)
Overview

This is a simple command-line Workout Tracker built in Python.
The goal of this project was to practice working with functions, lists, program structure, and basic CRUD operations (Create, Read, Update, Delete).

The application allows users to manage workouts directly from the terminal using a menu-based system.

Features

View all workouts

Add a new workout

Update sets, reps, or weight

Delete a workout

Exit the program safely

Handles empty workout list cases without crashing

Project Structure

The program is structured using functions for clarity and maintainability:

view_workouts(workouts) → Displays all workouts

add_workout(workouts) → Adds a new workout

update_workout(workouts) → Updates an existing workout

delete_workout(workouts) → Removes a workout

main() → Controls the menu system and program flow

The main() function acts as the central controller of the application.

Data Structure

Workouts are stored in a list.

Each workout is represented as:

[exercise_name, sets, reps, weight]


Example:

["Bench Press", 4, 8, 80]


The list is passed into functions so that all operations modify the same shared data.

Concepts Practiced

Functions and parameters

Mutable data types (lists)

Control flow (return, break)

While loops

Conditional logic

Avoiding code repetition (DRY principle)

Basic program architecture

Purpose of This Project

This project was built as part of a structured learning journey focused on mastering Python fundamentals and building toward larger end-to-end applications.

The main focus was understanding how to properly structure a program using functions and shared state.
