import unittest
from src.python.data_processors.cleaner import DataCleaner
from src.python.data_processors.transformer import DataTransformer

class TestDataProcessors(unittest.TestCase):

    def setUp(self):
        self.cleaner = DataCleaner()
        self.transformer = DataTransformer()

    def test_clean_data(self):
        raw_data = [
            {"id": 1, "value": "test"},
            {"id": 2, "value": None},
            {"id": 3, "value": "test2"},
        ]
        cleaned_data = self.cleaner.clean_data(raw_data)
        expected_data = [
            {"id": 1, "value": "test"},
            {"id": 3, "value": "test2"},
        ]
        self.assertEqual(cleaned_data, expected_data)

    def test_remove_duplicates(self):
        data_with_duplicates = [
            {"id": 1, "value": "test"},
            {"id": 1, "value": "test"},
            {"id": 2, "value": "test2"},
        ]
        unique_data = self.cleaner.remove_duplicates(data_with_duplicates)
        expected_data = [
            {"id": 1, "value": "test"},
            {"id": 2, "value": "test2"},
        ]
        self.assertEqual(unique_data, expected_data)

    def test_transform_data(self):
        raw_data = [
            {"id": 1, "value": "test"},
            {"id": 2, "value": "test2"},
        ]
        transformed_data = self.transformer.transform_data(raw_data)
        expected_data = [
            {"identifier": 1, "formatted_value": "TEST"},
            {"identifier": 2, "formatted_value": "TEST2"},
        ]
        self.assertEqual(transformed_data, expected_data)

    def test_format_data(self):
        data = [
            {"id": 1, "value": "test"},
            {"id": 2, "value": "test2"},
        ]
        formatted_data = self.transformer.format_data(data)
        expected_data = [
            {"id": 1, "formatted_value": "test"},
            {"id": 2, "formatted_value": "test2"},
        ]
        self.assertEqual(formatted_data, expected_data)

if __name__ == '__main__':
    unittest.main()