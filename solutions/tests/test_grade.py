#from ..grade import classStatistics, loadStudentData, saveData, studentAverage, viewGrades
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from grade import classStatistics, loadStudentData, saveData, studentAverage, viewGrades
import unittest
def test_loadStudentData():
    students = loadStudentData("grades.txt")
    assert students == {
        "Alice": [90, 85, 88],
        "Bob": [78, 82, 80],
        "Charlie": [92, 91, 94]
    }, f"Test failed for loadStudentData"

def test_viewGrades():
    students = {
        "Alice": [90, 85, 88],
        "Bob": [78, 82, 80]
    }
    # Check the printed output manually by running viewGrades function
    viewGrades(students)

def test_studentAverage():
    students = {
        "Alice": [90, 85, 88],
        "Bob": [78, 82, 80]
    }
    # Test for existing student
    studentAverage(students, "Alice")  # Expected output: 87.67
    # Test for non-existing student
    studentAverage(students, "David")  # Expected output: "Student 'David' not found."

def test_classStatistics():
    students = {
        "Alice": [90, 85, 88],
        "Bob": [78, 82, 80],
        "Charlie": [92, 91, 94]
    }
    classStatistics(students)

def test_saveData():
    students = {
        "Alice": [90, 85, 88],
        "Bob": [78, 82, 80]
    }
    saveData(students, "grades.txt")

# Run all tests
test_loadStudentData()
test_viewGrades()
test_studentAverage()
test_classStatistics()
test_saveData()

