  **PROJECT STATEMENT**


**PROBLEM STATEMENT**
Teachers and small institutions often need a quick way to record andtrack student information - personal details,subject-wise attendance,and academic performance - without the overhead of setting up a full database system or spreadsheet software. 
Manual tracking on paper is error-prone,hard to summarize,and doesn't easily calculate things like attendance percentage or grades.
This project addresses that gap with a lightweight,console-based Student Management System built using only core Python. It allows a teacher/admin to manage student records,mark subject-wise attendance,and record marks with automatic grade calculation - all through a simple,menu-driven interface,without relying on file storage or a database.

**SCOPE OF THE PROJECT**
The system operates as a single-session,in-memory application:data is available foe as long as the program runs and is not persisted between runs(no file handling or databae,per project constraints).
It supports management of multiple students, each with their own subject-wise attendance and marks.
The system is designed for a singleadmin/teacher user interacting through the console - it does not include multi-user login or authentication.
Core focus is on correctly applying fundamental programming concepts(functions,loops,conditionals,dictionaries,lists,exception handling) in a clean,modular way - not on building a production-grade,persistent system.

**TARGET USERS**
School or college teachers who want a simple digital tool to track a class of students.
Student learning core python who need a practical project demostrating functions, data structures, and modular program design.
Academic evaluators assessing correct application of subject fundamentals.

**HIGH LEVEL FEATURES**
1. *STUDENT RECORD MANAGEMENT*
    Add, view, search, update, and delete student records
2. *ATTENDANCE MANAGEMENT*
   Mark a student present/absent per subject
   View attendance history with automatically calculated percentage
   Warning flag when attendance drop below 75% in any subject
3. *MARKS & GRADE MANAGEMENT*
   Record marks per subject(0-100)
   Automatic letter-grade calculation(A+ to F)
   Generate a report card showing per-subject marks/grades and overall avreage/grade   