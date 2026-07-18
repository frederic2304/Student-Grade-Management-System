# Student-Grade-Management-System
1 Introduction
1.1 Background and Problem Statement
In educational institutions, manually managing students’ grades becomes increasingly difficult as
the number of students grows. Our project aims to automate this process by developing a Python-
based system that records student information, stores grades, automatically computes weighted
averages, and generates statistical reports.
1.2 Project Objectives
• Design an intuitive graphical user interface for data entry.
• Implement a weighted average calculation system.
• Generate individual report cards and class statistics.
• Comply with the technical requirements (no object-oriented programming, only basic data
structures).
2 Methodology
2.1 Problem Analysis
The system must manage:
• Four subjects with four assessments each.
• Different weight distributions (30% for E1/E2 and 20% for D1/D2).
• Missing grades.
• An overall ranking based on students’ averages.
1
2.2 Algorithmic Choices
We chose to use:
• Nested dictionaries to store grades.
• Lists to manage student records.
• Modular functions for each operation.
1 # Ranking display interface
2 def interface_afficher_classement () :
3 fen = tk . Toplevel ( root )
4 fen . title ( " Ranking " )
5 fen . geometry ( " 600 x400 " )
6 tree = ttk . Treeview ( fen ,
7 columns =( " name " , " average " ) ,
8 show = " headings " )
9 tree . heading ( " average " , text = " Average " )
10 tree . pack ( fill = " both " , expand = True )
11
12 # Average display interface
13 def interface_afficher_moyennes () :
14 fen = tk . Toplevel ( root )
15 fen . geometry ( " 400 x300 " )
16 text = tk . Text ( fen )
17 text . pack ( fill = " both " , expand = True )
Listing 1: Python Code Example
3 Implementation
3.1 Code Structure
• mainloop() : Manages the main menu.
• display() : Display functions.
• calculate() : Computation functions.
3.2 Challenges Encountered and Solutions
• Missing grades: handled using None values and filtering.
• Student ranking: implemented with itemgetter.
• Input validation: achieved through loops and exception handling.
• Development of the graphical interface using the tkinter library.
2
4 Results and Analysis
4.1 Results
The system provides:
• Unlimited student registration.
• Progressive grade entry.
• Automatic computation of class statistics.
• Generation of clear and readable reports.
4.2 Critical Analysis
• Strengths: intuitive graphical interface, modular code, robust error handling, and user-friendly
design.
• Weaknesses: data is not permanently stored.
5 Conclusion
Our system successfully meets the project requirements while providing a solid foundation for
future improvements. Possible enhancements include:
• Data persistence through file or database storage.
• Exporting reports and results to PDF format.
3
