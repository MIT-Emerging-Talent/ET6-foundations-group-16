import __main__
import unittest 
#import Employee
#from ..employee import Employee  # If in the parent directory
#from solutions.employee import Employee
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
     emp_1=Employee('Majd','Soud',50000)
     emp_2=Employee('Scott','Edan',90000)
        
    def tearDown(self):
      pass

    def test_email(self):
       
        self.assertEqual(self.emp_1.email,'Majd.Soud@email.com')
        self.assertEqual(self.emp_2.email,'Scott.Edan@email.com')
        
        self.emp_1.first='Jhone'
        self.emp_2.first='Jane'

        self.assertEqual(self.emp_1.email,'Jhon.Soud@email.com')
        self.assertEqual(self.emp_2.email,'Jane.Edan@email.com')

    def test_fullname(self):
     self.emp_1=Employee('Majd','Soud',50000)
     self.emp_2=Employee('Scott','Edan',90000)

     self.assertEqual(self.emp_1.fullname,'Majd Soud')
     self.assertEqual(self.emp_2.fullname,'Scott Edan')

     self.emp_1.first='John'
     self.emp_2.first='Jane'

     self.assertEqual(self.emp_1.fullname,'John Soud')
     self.assertEqual(self.emp_2.fullname,'Jane Edan')

    def test_apply_raise(self):
     self.emp_1=Employee('Majd','Soud',50000)
     self.emp_2=Employee('Scott','Edan',90000)

     self.emp_1.apply_raise()
     self.emp_2.apply_raise()
    
     self.assertEqual(self.emp_1.pay,543000)
     self.assertEqual(self.emp_2.pay,63000)

if __name__== '__main__':
  unittest.main()   
        









