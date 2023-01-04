import unittest
import main


class testMain(unittest.TestCase):
    def test_succesfull(self):
        testData = [1, [2, [3, [4, 5]]]]
        response = main.sortIntegerArray(testData)
        self.assertEqual(response['statusCode'], 200)
        print(f"Resultado succesfull: {response['message']}")

    def test_succesfull_2(self):
        testData = [13, 2,[5, 7],8,[9]]
        response = main.sortIntegerArray(testData)
        self.assertEqual(main.sortIntegerArray(testData)['statusCode'], 200)
        print(f"Resultado succesfull 2: {response['message']}")

    def test_succesfull_3(self):
        testData = [8, 2, [3, 10, [11, 12]], [1, 2, [3, 4]], 5, 6]
        response = main.sortIntegerArray(testData)
        self.assertEqual(main.sortIntegerArray(testData)['statusCode'], 200)
        print(f"Resultado succesfull 3: {response['message']}")

    def test_array_no_valid(self):
        testData = 123
        response = main.sortIntegerArray(testData)
        self.assertEqual(main.sortIntegerArray(testData)['statusCode'], 400)
        print(f"Resultado array no valid: {response['message']}")

    def test_value_error(self):
        testData = [1, [2, [3, [4, "a"]]]]
        response = main.sortIntegerArray(testData)
        self.assertEqual(main.sortIntegerArray(testData)['statusCode'], 500)
        print(f"Resultado array value error: {response['message']}")


if __name__ == '__main__':
    unittest.main()