# Test examples for leading_substrings function

import unittest
import tools

class Test_Leading_Substrings(unittest.TestCase):
    '''Tests for leading_substrings function.'''
    inputed = ''
    self.leading_substrings(inputted)
    output_expected = ['']
    self.assertEqual(output_expected, inputted, 'The string is empty')

if __name__ == '__main__':
    unittest.main()
