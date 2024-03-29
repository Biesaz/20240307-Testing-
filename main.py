# https://github.com/CodeAcademy-Online/python-new-material-level2/wiki/Testing:-lesson-1
# https://github.com/DonatasNoreika/python1lygis/wiki/UNIT-test%C5%B3-k%C5%ABrimas

# Testing: lesson 1
# MSkara edited this page on Jan 10 · 2 revisions
# Introduction
# When developing software, testing is an important part of ensuring that your code works as expected and meets the requirements. 
# In Python, the unittest module provides a framework for writing and running tests to validate the behavior of your code.

# With unittest, you can define a set of test cases, each of which tests a specific feature or behavior of your code. 
# Within each test case, you can define a set of test methods that verify that your code behaves as expected under 
# different conditions.

# Using unittest allows you to automate your tests, making it easier to run them repeatedly and catch regressions as 
# soon as they occur. unittest also provides powerful features for handling setup and teardown tasks, running test suites, 
# and reporting test results. Also improve your code quality.

# Overall, unittest is a powerful and flexible tool for testing your Python code and ensuring that it works correctly. 
# By investing time in writing tests, you can catch bugs early in the development process, save time on manual testing, 
# and ensure that your code is robust and reliable.

# Tests placement
# In Python projects that use unittest, tests are typically placed in a separate directory named tests or test. 
# Within this directory, tests are organized in a way that reflects the organization of the code being tested.

# For example, if your project has a module named my_module.py, you might create a file named test_my_module.py in 
# the tests directory to contain tests for that module.

# By separating tests from the main code, you can keep your codebase clean and focused on the main functionality, 
    # while the tests can be run independently and modified without affecting the main code.

# Examples
# after Testing a simple function:

# import unittest

# def add(a, b):
#     return a + b

# class TestAddFunction(unittest.TestCase):
    
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(0, 0), 0)
#         self.assertEqual(add(-1, 1), 0)
# Testing a class with setup and teardown:

# import unittest

# class Counter:
    
#     def __init__(self):
#         self.count = 0
        
#     def increment(self):
#         self.count += 1
        
#     def reset(self):
#         self.count = 0

# class TestCounter(unittest.TestCase):
    
#     def setUp(self):
#         self.counter = Counter()
        
#     def tearDown(self):
#         self.counter.reset()
        
#     def test_increment(self):
#         self.assertEqual(self.counter.count, 0)
#         self.counter.increment()
#         self.assertEqual(self.counter.count, 1)
#         self.counter.increment()
#         self.assertEqual(self.counter.count, 2)
# Testing an exception:

# import unittest

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     return a / b

# class TestDivideFunction(unittest.TestCase):
    
#     def test_divide(self):
#         self.assertEqual(divide(4, 2), 2)
#         self.assertRaises(ZeroDivisionError, divide, 4, 0)
# How to run
# In Python, you can run unittest tests using the command python -m unittest. This command will discover all the test 
# cases and test methods in your project and run them.

# Here's an example of how to use this command to run tests in a file named test_my_module.py:

# python -m unittest tests.test_my_module
# This command will run all the tests defined in the test_my_module.py file. You can also use wildcards to run all 
# tests in a directory or package:

# python -m unittest tests
# This command will run all tests in the tests directory.

# Note that if you are using a test runner other than unittest, the command to run tests may be different. 
# Check the documentation for your test runner to learn more.

# 1) Running all tests
# To run all tests in the test directory, you execute the following command from the project directory folder (python-unit-testing):

# python -m unittest discover -v
# Code language: Python (python)
# The discover is a subcommand that finds all the tests in the project.

# 2) Running a single test module
# To run a single test module, you use the following command:

# python -m unittest test_package.test_module -v
######################################### $ python -m unittest tests.test_kmi_skaiciavimas -v