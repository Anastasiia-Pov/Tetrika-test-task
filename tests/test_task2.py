import unittest
from unittest.mock import patch, MagicMock
from task2.solution import count_animals


class TestCountAnimals(unittest.TestCase):
    @patch('requests.get')
    def test_count_animals(self, mock_get):
        with open('html_for_test/task2_test_html_p1.html', 'r', encoding='utf-8') as f:
            page1_html = f.read()
        with open('html_for_test/task2_test_html_p2.html', 'r', encoding='utf-8') as f:
            page2_html = f.read()
        with open('html_for_test/task2_test_html_p3.html', 'r', encoding='utf-8') as f:
            page3_html = f.read()

        mock_get.side_effect = [
            MagicMock(text=page1_html),
            MagicMock(text=page2_html),
            MagicMock(text=page3_html),
        ]

        expected_result = {
            'А': 6,
            'Б': 3
        }

        fake_url = "https://test_task_tetrika.com"
        test_result = count_animals(fake_url)

        self.assertEqual(test_result, expected_result)


if __name__ == '__main__':
    unittest.main()
