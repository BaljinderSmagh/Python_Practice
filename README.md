# Writing a Code In a Clean and Modular way
  * Use meaningful names for variables and functions.
  * Long Names doesn't imply descriptive names
  * Avoid using abbrevations and single letters names.
  * For Boolean variables, it helpful to use a prefix with the name like 'is_effective' or 'has_effective'.
  * Organize your code line with consistent indentation(standard is to use four space for each indent).
  * Try to separate the different sections of your code with blank lines.
  * Try to keep your lines to roughly 79 characters, which is the PEP 8 style guide's recommendation.
  * Including Docstring to explain the functionality of any function in yor code.

# How to make your code efficient?
  * Reducing run time.
  * Reducing space it occupies in memory.
  
# Testing the Code
  * Testing your code is important before deploying it to production.
  * Unexpected data can break your given assumptions.
  * You can write test cases to check your code.
  * We can use unit Testing to avoid writing repeatable code for testing and it is isolated from the your main code.
  * Pytest is a python library you can for unit testing. it will run all the tests even one of the test set fails.
  * Test driven Development where you write the test cases before writing main code.

# Logging messages
  * Use normal capitalization for messages. 
  * Debug: To talk about things happening (such as when,where and how this occurred) in the program.
  * Error: To record the errors occurring in the program.
  * Info: To record all the actions such as regularly scheduled operations.

# Conducting the Code Review
  * While you can above points when reviewing a code. To save time, you can use python code linter like pylint which can automatically check for coding standards
    and PEP 8 guidelines.


## Citations
* Software Engineering Practice by Udacity
