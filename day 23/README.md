__File Handling & JSON Practice (Python)__
__Overview__

This project focuses on practicing basic file handling and working with JSON in Python.

The goal was to understand how to:

- Create and write to a text file

- Read data from a text file

- Store structured data using JSON

- Load JSON data back into a Python program

This is part of my ongoing journey to strengthen core Python fundamentals.

__Project Structure__

The project contains two simple exercises:

__1. Basic Text File Handling__

- Create a file (hello.txt)

- Write text into the file

- Open and read the file

- Print the contents to the console

This exercise helped reinforce how file modes work:

- "w" → write mode

- "r" → read mode

It also introduced the use of context managers (with open(...) as f) for safe file handling.

__2. Working with JSON__

- Create a Python dictionary

- Save it to a .json file using json.dump()

- Load the JSON file using json.load()

- Access specific values from the loaded data

Example structure used:

{
  "naam": "nick",
  "age": 27,
  "gym": "yes"
}

This demonstrates how structured data can be stored outside of the program and reused later.

__Concepts Practiced__

- File creation and reading

- File modes (r, w)

- Context managers (with statement)

- Dictionaries

- JSON serialization (json.dump)

- JSON deserialization (json.load)

- Accessing dictionary values

__Purpose of This Project__

This project is part of building strong fundamentals in Python before moving toward larger applications.

Understanding file handling and JSON is essential for:

- Saving data

- Persisting application state

- Preparing for backend and API development
