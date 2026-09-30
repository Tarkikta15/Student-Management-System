   **STUDENT MANAGEMENT SYSTEM**

A.**OVERVIEW**
A menu driven, console-based Student Management System built entirely with **core Python**- no file handling , no databases, no external libraries. All student data(records, attendance,marks) is stored in memory using Python lists and dictionaries for the duration of a single program run.
This project was built to demostrate practical application of fundamental programming concepts:control flow, funvtions, data structures, input validation, and modular code organization across multiple files.

B.**FEATURES**
1. *Student Records Management*
a. Add a new student(roll number, name, class)
b. View all students in a formatted table
c. Search for a student by roll number
d. Update an existing student's details
e. Delete a student record

2. *Attendance Management (Subject-wise)*
a. Mark daily attendance for a student, per subject(e.g. Maths,Physics)
b. Automatically tracks present count vs total classes per subject
c. View a student's full attendance record with calculated percentage
d. Flags subjects where attendance falls below 75%

3. *Marks & Grade Management (Subject-wise)*
a. Enter marks (out of 100) for a student in a given subject
b. Automatic grade calculation(A+,A,B,C,D,F) based on marks
c. View a complete report card with per-subject marks,grades,overall average, and overall grade

C.**TECHNOLOGIES/TOOLS USED**
a. *Language*: Python 3
b. *Concepts used*: functions,loops(for, while), conditionals(if/elif/else), lists, dictionaries, string formatting with .format(), exception handling(try/except),module imports
c. *No external libraries*- built entirely with Python's standard,built-in features
d. *No f-strings*- formatting is done with str.format() to match what has been covered in class
e. *Editor*: VS Code
f. *Version control*: Git/GitHub

D. **STEPS TO INSTALL AND RUN**
1. Ensure Python 3 is installed on your system.
2. Clone this repository or download all files into a single folder.
3. Open the folder in VS Code (or any terminal).
4. Run the application.
5. Use the on-screen numbered menu to navigate between features.

E. **INSTRUCTIONS FOR TESTING**
 *Add Students* - choose option 1, add 2-3 students with different roll numbers.
 *View Students* - choose option to confirm they were added correctly.
 *Search/Update/Delete* - try options 3,4,5 on an existing roll number,and also try an invalid roll number to confirm error handling works.
 *Mark Attendance* - choose option 6, mark a student present/absent in a few different subjects across multiple "days"(repeat the option).
 *View Attendance* - choose option 7 to confirm the present/total counts and percentage are correct, and that the <75% warning appears when expected.
 *Enter Marks* - choose option 8 for a few subjects for one student.
 *View Report Card* - choose option 9 to confirm grades and average are calculated correctly.
 *Invalid Input Testing* - try entering letters instead of numbers where a roll number or marks are expected,to confirm the program doesn't crash.

 F.**LIMITATIONS & FUTURE ENHANCEMENTS**
 1. Data is stored only in memory and is lost when the programs exits(by design, per projectt constraints - no file handling/database allowed).
 2. Future enhancement: Data-wise attendance history instead of just present/total counts.
                        Add persistent storage(file-based or database) once permitted.
                        Export report cards or attendance summaries as text/CSV output.

G.**SCREENSHOTS**
 ##addstudent
 ![Add student](screenshot/add%20student.png)

 ##viewallstudents
 ![View student](screenshot/view%20all%20students.png)

 ##searchstudent
 ![Search student](screenshot/search%20student.png)

 ##updatestudent
 ![Update student](screenshot/update%20student.png)

 ##markattendance
 ![Mark attendance](screenshot/mark%20attendance.png)

 ##viewattendance
 ![View attendance](screenshot/view%20attendance.png)

 ##marks
 ![Marks](screenshot/marks.png)

 ##reportcard
 ![Report card](screenshot/report%20card.png)