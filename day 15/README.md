Day 14 Project
📌 Project: Student Grade Manager (CLI)

A simple command-line application built in Python to manage student names and grades.

🎯 Purpose

This project was created to:

Practice working with nested lists

Strengthen menu-based program logic

Improve handling of user input

Debug and fix structural data errors

🧠 Concepts Practiced

while loops

if / elif / else

Lists and nested lists

enumerate()

Index manipulation (index = user_input - 1)

String vs Integer conversion

Debugging structural bugs

⚙️ Features

View Students

Displays all students with index number and grade.

Handles empty list case.

Add Student

Prompts for student name and grade.

Stores data as a nested list:

[name, grade]


Update Grade

Select student by number.

Update grade using index reference:

students[index][1] = newgrade


Remove Student

Select student by number.

Remove using:

students.pop(index)


Exit Program

🐛 Bugs Fixed During Development
1️⃣ Incorrect List Structure

❌ Initial mistake:

students.append(user_inp1)
students.append(user_inp2)


This created separate list entries instead of grouped student data.

✅ Correct solution:

students.append([user_inp1, user_inp2])


This properly grouped each student with their grade.

2️⃣ String vs Integer Error

Problem:

user_inp - 1


input() returns a string, causing a TypeError.

Solution:

user_inp = int(input(...))
index = user_inp - 1


Converted string input to integer before performing arithmetic.

🚀 Key Learning

Today reinforced an important lesson:

Understanding how data is structured is more important than writing more code.

Nested lists, indexing, and correct data types are fundamental for building more complex systems later.
