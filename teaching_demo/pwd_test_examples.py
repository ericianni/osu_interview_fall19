import unittest
from password_check import password_check
'''
Password Specifications
* Between 8-20 characters (inclusive)
* At least one special character - '@', '#', '$', '%', '&', '*', '!'
* At least one uppercase letter
* At least one lowercase letter
'''
class MyTestCase(unittest.TestCase):
    # len(short), sym, digit, upper, lower
    def test_short(self):
        self.assertFalse(password_check('He11@'), msg='He11@ does not meet requirements')

    # len(long), sym, digit, upper, lower
    def test_long(self):
        self.assertFalse(password_check('He11@dsfdjasklasasfdsa'), msg='He11@dsfdjasklasasfdsa does not meet requirements')

    # len, sym(*), digit, upper, lower
    def test_sym(self):
        self.assertFalse(password_check('Pas5word'), msg='Pas5word does not meet requirements')

    # len, sym, digit(*), upper, lower
    def test_digit(self):
        self.assertFalse(password_check('Pas$word'), msg='Pas$word does not meet requirements')

    # len, sym, digit, upper(*), lower
    def test_upper(self):
        self.assertFalse(password_check('pa$5word'), msg='pa$5word does not meet requirements')

    # len, sym, digit, upper, lower(*)
    def test_lower(self):
        self.assertFalse(password_check('PA$5WORD'), msg='PA$5WORD does not meet requirements')

    # len(8), sym, digit, upper, lower
    def test_len_8(self):
        self.assertTrue(password_check('Pa$5word'), msg='Pa$%word meets the requirements')

    # len(20), sym, digit, upper, lower
    def test_len_20(self):
        self.assertTrue(password_check('This!$MyPassword1234'), msg='This!$MyPassword1234 meets the requirements')

if __name__ == '__main__':
    unittest.main(verbosity=2)
