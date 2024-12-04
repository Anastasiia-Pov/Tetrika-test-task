import unittest
from task1.solution import strict

class TestTypeDecorator(unittest.TestCase):

    def test_ints_correct_arguments(self):
        @strict
        def sum_int(a: int, b: int, c: int) -> int:
            return a + b - c

        self.assertEqual(sum_int(1, 2, 2), 1)
        self.assertEqual(sum_int(4, 3, 1), 6)

    def test_ints_incorrect_argument_str(self):
        @strict
        def sum_int(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError):
            sum_int(1, "4")

    def test_ints_incorrect_argument_float(self):
        @strict
        def sum_int(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError):
            sum_int(1, 4.5)

    def test_int_float(self):
        @strict
        def check_mixed_types(a: int, b: float, c: int) -> float:
            return a + b + c

        self.assertEqual(check_mixed_types(1, 2.5, 1), 4.5)
        with self.assertRaises(TypeError):
            check_mixed_types("1", 2.5, "1")

    def test_incorrect_result(self):
        @strict
        def check_mixed_types(a: int, b: int, c: float) -> str:
            return a + b + c

        with self.assertRaises(TypeError):
            check_mixed_types(2, 2, 2.0)

    def test_correct_result(self):
        @strict
        def check_mixed_types(a: int, b: str) -> str:
            return b * a

        self.assertEqual(check_mixed_types(2, 'plus'), 'plusplus')

    def test_correct_string_result(self):
        @strict
        def check_string(a: str, b: int, c: float, d: bool) -> str:
            return f"{a} {b} {c} {d}"

        self.assertEqual(check_string('one', 1, 1.0, True), 'one 1 1.0 True')

    def test_bools(self):
        @strict
        def changed_bools(a: bool) -> bool:
            return not a

        self.assertTrue(changed_bools(False))
        self.assertFalse(changed_bools(True))
        with self.assertRaises(TypeError):
            changed_bools(1)

    def test_not_annotated_func(self):
        @strict
        def check_not_annotated(a, b, c):
            return a + b + c

        self.assertEqual(check_not_annotated(1, 2, 3), 6)
        with self.assertRaises(TypeError):
            check_not_annotated(1, ' plus ', 3)

