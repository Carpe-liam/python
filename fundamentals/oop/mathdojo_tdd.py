import unittest

def add_func(self,num,*nums):
    for n in nums:
        self.result += n
    self.result += num
    return self

class add_funcTest(unittest.TestCase):    
    def test1(self):
        self.assertEqual(add_func(4,5), 9)

def setUp(self):
    print("setting up")
    class MathDojo:
        def __init__(self):
            self.result = 0


        def subtract(self, num, *nums):
            for n in nums:
                self.result -= n
            self.result -= num
            return self



def tearDown(self):
    print('tearing down')

if __name__ == '__main__': 
    unittest.main()