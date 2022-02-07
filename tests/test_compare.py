import unittest
from compare import compare_line, compare_lines, is_eof_lf, validate_answer, NotEofLfException, WrongAnswerException

class CompareLineTests(unittest.TestCase):
    def test_compare_line(self):
        answer_line = '1 4 7 10\n'
        output_line = '1 4 7 10\n'
        self.assertIsNone(compare_line(answer_line, output_line))
    
    def test_compare_line_with_endspace(self):
        answer_line = '1 4 7 10 \n'
        output_line = '1 4 7 10\n'
        self.assertIsNone(compare_line(answer_line, output_line))
    
    def test_compare_line_not_eq(self):
        answer_line = 'fail'
        output_line = '1 4 7 10\n'
        with self.assertRaises(Exception):
            compare_line(answer_line, output_line)


class CompareLinesTests(unittest.TestCase):
    def test_compare_lines(self):
        answer_filepath = './tests/answers/1.txt'
        output_filepath = './tests/outputs/1.txt'
        self.assertTrue
        (compare_lines(answer_filepath, output_filepath))
    
    def test_compare_lines_with_index_error(self):
        answer_filepath = './tests/answers/fail1.txt'
        output_filepath = './tests/outputs/1.txt'
        with self.assertRaises(WrongAnswerException):
            compare_lines(answer_filepath, output_filepath)


class IsEosLfTests(unittest.TestCase):
    def test_is_eof_lf(self):
        filepath = './tests/answers/1.txt'
        self.assertIsNone(is_eof_lf(filepath))

    def test_is_eof_lf_fail(self):
        filepath = './tests/answers/fail2.txt'
        with self.assertRaises(NotEofLfException):
            is_eof_lf(filepath)


class ValidateAnswerTests(unittest.TestCase):
    def test_validate_answer(self):
        answer_filepath = './tests/answers/1.txt'
        output_filepath = './tests/outputs/1.txt'
        self.assertIsNone(validate_answer(answer_filepath, output_filepath))
    
    def test_validate_anwer_raise_eof_lf(self):
        answer_filepath = './tests/answers/fail2.txt'
        output_filepath = './tests/outputs/1.txt'
        with self.assertRaises(NotEofLfException):
            validate_answer(answer_filepath, output_filepath)
    
    def test_validate_answer_raise_wrong_answer(self):
        answer_filepath = './tests/answers/wrong1.txt'
        output_filepath = './tests/outputs/1.txt'
        with self.assertRaises(WrongAnswerException):
            validate_answer(answer_filepath, output_filepath)
