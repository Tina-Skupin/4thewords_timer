import unittest
from src.main import calculate_actual_battle_count  # import the function you want to test

class TestMain(unittest.TestCase):
    
    def test_act_battle_count(self):
        result = calculate_actual_battle_count(100, 1000)
        self.assertEqual(result, 500)

    def test_act_battle_count2(self):
        result = calculate_actual_battle_count(10, 1000)
        self.assertEqual(result, 909)

if __name__ == '__main__':
    unittest.main()