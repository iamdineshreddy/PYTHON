# Assignment – Python Data Structures (Dictionary & List Slicing)

## 📌 Overview
This repository contains Python programs demonstrating the use of:
- **Dictionaries** for storing and retrieving data
- **List slicing** for extracting and manipulating list elements

The programs include proper validation, clear logic, and are written in a beginner-friendly manner.

---

## 📂 Repository Structure

Python-Assignment/
│
├── task_student_marks.py
├── task_list_slicing.py
└── README.md

markdown
Copy code

---

## 🧑‍🎓 Task 1: Create a Dictionary of Student Marks

### 🔹 Description
- Creates a dictionary where **student names are keys** and **their marks are values**.
- Takes a student name as input from the user.
- Retrieves and displays the corresponding marks.
- Displays an appropriate message if the student name does not exist.

### 🔹 Key Concepts Used
- Python dictionaries
- Conditional checks
- User input handling
- Error prevention (`KeyError` avoided)

### 🔹 Sample Output

**If the student exists:**
Enter the student's name: Alice
Marks obtained by Alice: 85

markdown
Copy code

**If the student does not exist:**
Enter the student's name: John
Student not found in the records.

markdown
Copy code

---

## 🔢 Task 2: Demonstrate List Slicing

### 🔹 Description
- Creates a list of numbers from **1 to 10**.
- Extracts the **first five elements** using list slicing.
- Reverses the extracted elements.
- Prints both the extracted list and the reversed list.

### 🔹 Key Concepts Used
- List creation using `range()`
- List slicing
- Reversing lists with slicing

### 🔹 Sample Output
Extracted list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]

yaml
Copy code

---

## 🧪 Testing & Validation

The programs were tested with:
- Valid inputs
- Invalid inputs (non-existing student names)
- Edge cases (empty input)

### ✔ Validations Implemented
- Checks for student existence in dictionary
- Case-insensitive input handling
- Safe list slicing without errors

---

## ▶️ How to Run the Programs

1. Clone the repository:
   ```bash
   git clone <your-github-repository-link>
Navigate to the project folder:

bash
Copy code
cd Python-Assignment
Run the scripts:

bash
Copy code
python task_student_marks.py
python task_list_slicing.py
