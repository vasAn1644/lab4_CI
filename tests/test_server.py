import unittest
import os
import json
from server import split_text, read_json_with_limit

class TestServerFunctions(unittest.TestCase):
    
    def setUp(self):
        """Налаштування перед кожним тестом."""
        # Створюємо тимчасовий JSON-файл для тестування
        self.test_json_path = "test_data.json"
        with open(self.test_json_path, "w", encoding="utf-8") as f:
            json.dump({"messages": [{"text": "Hello"}, {"text": "World"}]}, f)
    
    def tearDown(self):
        """Очищення після кожного тесту."""
        if os.path.exists(self.test_json_path):
            os.remove(self.test_json_path)
    
    def test_split_text_short(self):
        """Тестування split_text із коротким текстом."""
        text = "Hello world"
        result = split_text(text, max_length=20)
        text = text.split(" ")
        self.assertEqual(result, text )
    
    def test_split_text_long(self):
        """Тестування split_text із довгим текстом."""
        text = "Hello\nworld\nthis\nis\na\ntest"
        result = split_text(text, max_length=10)
        self.assertEqual(result, ["Hello", "world", "this", "is", "a", "test"])
    
    def test_read_json_with_limit_small_file(self):
        """Тестування read_json_with_limit із малим файлом."""
        result = read_json_with_limit(self.test_json_path, max_size_kb=10, max_messages=1)
        self.assertEqual(len(result["messages"]), 2)  # Файл малий, повертає всі повідомлення
    
    def test_read_json_with_limit_large_file(self):
        """Тестування read_json_with_limit із великим файлом (імітація)."""
        # Імітуємо великий файл, встановивши низький max_size_kb
        result = read_json_with_limit(self.test_json_path, max_size_kb=0.001, max_messages=1)
        self.assertEqual(len(result["messages"]), 1)  # Повертає лише 1 останнє повідомлення

if __name__ == '__main__':
    unittest.main()