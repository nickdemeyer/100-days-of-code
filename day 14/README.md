# Day 14 — Simple Library Manager (Python)

## 📌 Overview
This project is part of my daily Python learning journey.

Instead of learning new concepts, Day 14 focused on **deeply applying existing fundamentals**, especially:
- lists
- nested lists
- updating program state
- thinking in indexes instead of variables

The project took nearly two hours due to logical challenges, not syntax issues.

---

## 📚 Project: Simple Library Manager

A command-line application that manages a small library of books.

Each book is stored as a list:
[titel, status]

All books are stored inside one main list:
books = []

---

## ⚙️ Features

The user can:

1. **View books**
   - Shows all books with a number, title, and status
   - Displays a message if the library is empty

2. **Add book**
   - Asks for a book title
   - Automatically sets status to `"available"`

3. **Borrow book**
   - Shows all books
   - User selects a book by number
   - If the book is available, its status changes to `"borrowed"`
   - If already borrowed, a message is shown

4. **Return book**
   - Similar to borrow
   - Changes status from `"borrowed"` back to `"available"`

5. **Exit**
   - Stops the program

---

## 🧠 Key Learning Points

- Understanding that **program state lives inside data structures**
- Avoiding reliance on loose variables for important data
- Working with nested lists using indexes:
  - `book[0]` → title
  - `book[1]` → status
- Updating values directly inside a list:
  - `books[index][1] = "borrowed"`

This project highlighted how important it is to build a clear mental model of how data changes over time.

---

## 🧪 Concepts Used

- Variables
- Lists
- Nested lists
- while loops
- if / elif / else
- enumerate
- Index-based updates


