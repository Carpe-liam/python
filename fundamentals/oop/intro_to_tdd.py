    #import UnitTest
import unittest

def revList(list):
    pass
    newList = []
    for i in range(len(list)-1, -1, -1):
        newList.append(list[i])
    return newList

def isPalindrome(str):
    str = str.lower()
    for l in range(0, int(len(str)/2)):
        if str[l] != str[len(str)-l-1]:
            return False
        else:
            return True

def coins(cash):
    pass


    #UNIT TESTS
class revListTest(unittest.TestCase):
    #first method - reverse method test
    def testOne(self):
        self.assertEqual(revList([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(revList([5,4,1]), [1,4,5])
    def testThree(self):
        self.assertEqual(revList([5,9,1,3,4]), [4,3,1,9,5])
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

class isPalindromeTest(unittest.TestCase):
    #first method - reverse method test
    def testOne(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def testTwo(self):
        self.assertEqual(isPalindrome("Aviddiva"), True)
    def testThree(self):
        self.assertEqual(isPalindrome("Madam"), True)
    def testFour(self):
        self.assertEqual(isPalindrome("rotator"), True)
    def testFive(self):
        self.assertEqual(isPalindrome("anna"), True)


class coinsTest(unittest.TestCase):
    #first method - reverse method test
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])


    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main() # this runs our tests