# Test examples for leading_substrings function

import unittest
import leading

class Test_Leading_Substrings(unittest.TestCase):
    '''Tests for leading_substrings function.'''

    def test_empty_string(self):
        '''Test empty string'''
        inputed = ''
        output = leading.leading_substrings(inputed)
        output_expected = []
        self.assertEqual(output, output_expected, 'The string is empty.')

    def test_one_characte_string(self):
        '''Test on a one-character string.'''
        inputed = 'a'
        output = leading.leading_substrings(inputed)
        output_expected = ['a']
        self.assertEqual(output, output_expected, 'The string is of length 1.')

    def test_longer_string(self):
        '''Test on a longer string.'''
        inputed = 'hello'
        output = leading.leading_substrings(inputed)
        output_expected = ['h', 'he', 'hel', 'hell', 'hello']
        self.assertEqual(output, output_expected, 'The string is longer.')

if __name__ == '__main__':
    unittest.main()
