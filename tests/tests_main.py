import unittest
from src.main import calculate_actual_battle_count, words_to_minutes  # import the function you want to test

class TestMain(unittest.TestCase):
    
    def test_act_battle_count(self):
        result = calculate_actual_battle_count(100, 1000)
        self.assertEqual(result, 500)

    def test_act_battle_count2(self):
        result = calculate_actual_battle_count(10, 1000)
        self.assertEqual(result, 909)


    def test_words_to_minutes1(self):
        result = words_to_minutes(500)
        self.assertEqual(result, 30)

    def test_words_to_minutes2(self):
        result = words_to_minutes(2000)
        self.assertEqual(result, 120)


if __name__ == '__main__':
    unittest.main()