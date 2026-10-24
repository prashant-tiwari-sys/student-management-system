
# Student Performance & Management System

## 1. Project Description

The Student Performance & Management System is a beginner-friendly Python console application that helps manage student information and academic performance.

It allows users to add, view, search, update, and delete student records. It also calculates student averages and grades and generates a performance summary.

Student records are stored in a JSON file, allowing data to remain available when the application is restarted.

## 2. Features

- Add new student records
- View all student records
- Search for a student using their ID
- Update student marks
- Delete student records
- Calculate average marks and grades
- Display an academic performance summary
- Identify scholarship-eligible students
- Store data using JSON file handling
- Handle invalid input and file errors
- Save the date and time when a student is added

## 3. Technologies Used

- **Programming Language:** Python
- **Data Storage:** JSON
- **Version Control:** Git
- **Code Hosting:** GitHub
- **Libraries:** `json`, `os`, `datetime`
- **OOP Module:** `abc`

No third-party Python packages are required.

## 4. Python Concepts Covered

| Concept | Application in the Project |
|---|---|
| Variables and data types | Student details, marks, IDs and choices |
| Input and output | `input()` and `print()` |
| Operators | Arithmetic and comparison operators |
| Type casting | `int()` and `float()` |
| Conditional statements | `if`, `elif` and `else` |
| Loops | `for` and `while` |
| Functions | Add, search, update and delete operations |
| Data structures | Lists, dictionaries and tuples |
| File handling | Reading and writing JSON data |
| Exception handling | `try`, `except` and file error handling |
| Libraries | `json`, `os` and `datetime` |
| Classes and objects | `Person`, `Student` and `ScholarshipStudent` |
| Constructor | `__init__()` |
| Inheritance | `Student` inherits from `Person` |
| Polymorphism | Overridden `get_details()` method |
| Encapsulation | Private student ID and `@property` |
| Abstraction | Abstract `Person` class and `get_details()` |
| Git | Tracking changes and creating commits |
| GitHub | Hosting and sharing the project repository |

## 5. Project Structure

```text
student_management_system/
├── main.py
├── student.py
├── README.md
├── requirements.txt
├── .gitignore
└── data/
    └── .gitkeep
```

The `data/students.json` file is created automatically when student records are saved.

## 6. How to Run the Project

### Requirements

- Python 3 installed
- Git installed (for version control)
- A code editor such as VS Code (optional)

### Step 1: Download or clone the project

If you have cloned the GitHub repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student_management_system
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 2: Run the application

Open a terminal in the project folder and execute:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

### Step 3: Use the menu

Choose an option from the displayed menu:

1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Performance Summary
7. Exit

Follow the instructions displayed in the terminal.

## 7. Git and GitHub Setup

Configure Git with your own name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Initialize the repository and upload the project:

```bash
git init
git status
git add .
git commit -m "Initial student management system"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Create an empty repository on GitHub first. Replace the repository URL with your actual URL.

If the remote already exists, do not add it a second time.

## 8. Screenshots
<img width="629" height="345" alt="image" src="https://github.com/user-attachments/assets/8976447b-2cc2-4aa6-859c-de8540645b4e" />
<img width="1307" height="886" alt="image" src="https://github.com/user-attachments/assets/b56bac89-0c98-4c73-a61c-8280cba0ef44" />
<img width="1307" height="886" alt="image" src="https://github.com/user-attachments/assets/ab0873ba-e77e-442a-8319-78b406a8877d" />
<img width="1900" height="920" alt="image" src="https://github.com/user-attachments/assets/1f279ffa-4bf8-4fe9-85df-93093fcb190a" />


## 9. Challenges Faced

- Validating user input
- Handling invalid marks and ages
- Managing student records
- Saving and loading data from a file
- Handling missing or invalid JSON data
- Understanding object-oriented programming
- Learning Git commands and GitHub repository management

## 10. Future Improvements

- Add a graphical user interface using Tkinter
- Add login authentication for administrators
- Generate PDF student report cards
- Export student data to CSV or Excel
- Add subject-wise performance charts
- Add a database such as MySQL or SQLite
- Improve searching and sorting features

## 11. Conclusion

The Student Performance & Management System demonstrates how Python can be used to build a practical application for managing student records.

The project combines fundamental programming concepts, file handling, exception handling, object-oriented programming, and version control using Git and GitHub.

It provides a foundation for developing more advanced student management applications in the future.
