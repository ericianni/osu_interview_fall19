import unittest
from password_check import password_check
'''
Password Specifications
* Between 8-20 characters (inclusive)
* At least one special character - '!', '@', '#', '$', '%', '&', '*'
* At least one uppercase letter
* At least one lowercase letter
'''
class MyTestCase(unittest.TestCase):
    def test_short(self):
        self.assertFalse(password_check('hello'), msg='hello does not meet requirements')

if __name__ == '__main__':
    unittest.main(verbosity=2)
