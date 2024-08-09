Problem statement:
Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

Objective :
The objective of this Python program is to efficiently manage and analyze the marks scored by students in the subject “Fundamental of Data Structure.” The program aims to:
1.	Store and organize the marks of N students in a structured manner.
2.	Compute and display the average score of the class to understand the overall performance.
3.	Identify and display the highest and lowest scores to highlight the range of marks.
4.	Count and report the number of students who were absent for the test, ensuring accurate record-keeping.
5.	Determine and display the mark with the highest frequency to identify common performance trends among students.

Outcome:
Data Collection: It prompts the user to enter the number of students and then records each student’s mark or an indication of absence (entered as 'A').
•	Compute Average Score: The program calculates the average score of the class by summing all the valid marks and dividing by the total number of students who were present.
•	Find Highest and Lowest Scores: It identifies the highest and lowest scores among the students who were present for the test, providing insights into the performance range of the class.
•	Count Absent Students: It counts how many students were absent by tallying the 'A' entries, helping in understanding attendance patterns.
•	Mark with Highest Frequency: Using the Counter from the collections module, the program determines which mark was most frequently recorded, highlighting the most common performance level.


Data Collection: It prompts the user to enter the number of students and then records each student’s mark or an indication of absence (entered as 'A'). .
•	Compute Average Score: The program calculates the average score of the class by summing all the valid marks and dividing by the total number of students who were present.
•	Find Highest and Lowest Scores: It identifies the highest and lowest scores among the students who were present for the test, providing insights into the performance range of the class.
•	Count Absent Students: It counts how many students were absent by tallying the 'A' entries, helping in understanding attendance patterns.
•	Mark with Highest Frequency: Using the Counter from the collections module, the program determines which mark was most frequently recorded, highlighting the most common performance level.


4) Software & Hardware requirerments :
Software Requirements:
•	Python Interpreter: Python 3.6 or later.
•	IDE/Text Editor: PyCharm, Visual Studio Code, or any text editor.
•	Libraries: Standard Python libraries (no additional installation needed).

Hardware Requirements:
•	Processor: Modern CPU (e.g., Intel Core i3 or AMD Ryzen 3).
•	Memory (RAM): Minimum 2 GB, recommended 4 GB.
•	Storage: Minimum 10 MB, recommended 100 MB for additional files.
•	Display: Standard resolution (1366x768 or higher).
•	Internet Connection: Optional, for downloading Python and IDE.

Theory:
Python Programming: Python is a high-level, interpreted programming language known for its readability and simplicity. It supports various programming paradigms including procedural, object-oriented, and functional programming.
Data Handling in Python:•	Lists: Used to store multiple items in a single variable. For example, storing student marks.
•	Standard Libraries: Python’s built-in libraries (like collections.Counter) help manage and analyze data efficiently.
•	Lists: Used to store multiple items in a single variable. For example, storing student marks.
•	Standard Libraries: Python’s built-in libraries (like collections.Counter) help manage and analyze data efficiently.

Defining a Function
You define a function using the def keyword, followed by the function name and parentheses.
Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
Some Benefits of Using Functions
•	Increase Code Readability 
•	Increase Code Reusability

Python Function Declaration:
Types of Functions in Python are-
•	Built-in library function: These are Standard functions in Python that are available to use.
•	User-defined function: We can create our own functions based on our requirements.

Creating a Function in Python:
We can define a function in Python, using the def keyword. We can add any type of functionalities and properties to it as we require. By the following example, we can understand how to write a function in Python. In this way we can create Python function definition by using def keyword.

Calling a Function in Python:
After creating a function in Python we can call it by using the name of the functions Python followed by parenthesis containing parameters of that particular function. Below is the example for calling def function Python.
# A simple Python function
def fun():
    print("Welcome to GFG")
# Driver code to call a function
fun()

Algorithm:
1.	Start
2.	Input Number of Students (N)
3.	Initialize marks list and absent_count to 0
4.	For each student from 1 to N:
        Input student mark or absence ('A')
        If input is 'A':
            Increment absent_count by 1
        Else:
            Try to convert input to a float
            If successful, append mark to marks list
            If unsuccessful, print an error message
5.	Compute Average Score:
       If marks list is not empty:
           Calculate average as sum of marks divided by the length of marks
       Else:
           Set average to 0
6.	Find Highest and Lowest Scores:
        If marks list is not empty:
            Determine highest score using max()
            Determine lowest score using min()
        Else:
            Set highest and lowest to None
7.	Find Mark with Highest Frequency:
        If marks list is not empty:
              Use Counter from collections to find the most common mark
         Else:
              Set most frequent mark to None
8.	Display Results:
        Number of students absent
        Average score
        Highest score
        Lowest score
        Mark with highest frequency
9.	End
	
Concluion :
The Python program efficiently tracks and analyzes student marks for "Fundamental of Data Structure." It computes the average score, highest and lowest marks, counts absentees, and 
•	Else: Set both to None
7.	Find Mark with Highest Frequency:
•	If marks is not empty: Use Counter to find the most frequent mark
•	Else: Set most frequent mark to None
8.	Display Results:
•	Absent count
•	Average score
•	Highest score
•	Lowest score
•	Most frequent mark
9.	End




7) Concluion :
The Python program efficiently tracks and analyzes student marks for "Fundamental of Data Structure." It computes the average score, highest and lowest marks, counts absentees, and identifies the most frequent mark, providing a clear overview of class performance and attendance for effective educational management.
