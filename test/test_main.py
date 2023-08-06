import unittest # The test framework

class Test_Main(unittest.TestCase):
    def test_main1(self):
        self.assertEqual(3,3)
    
    def test_main2(self):
        self.assertEqual(4,4)

if __name__ == '__main__':
    unittest.main()