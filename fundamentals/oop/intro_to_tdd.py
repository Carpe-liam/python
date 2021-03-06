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
    coin_type = {'quarters': 25, 'dimes': 10, 'nickels': 5, 'pennys': 1}
    change = {}
    for coin in coin_type:
        if coin_type[coin] <= cash:
            change[coin] = cash//coin_type[coin]
            cash = cash%coin_type[coin]
        else:
            change[coin] = 0
    x = []
    for coin in change:
        x.append(change[coin])
    return x

def factorial_Func(num):
    if num == 1:
        return num
    elif num < 0: 
        return False
    else:
        return num*factorial_Func(num-1)


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
    def test1(self):
        self.assertEqual(coins(87), [3,1,0,2])
    def test2(self):
        self.assertEqual(coins(50), [2,0,0,0])
    def test3(self):
        self.assertEqual(coins(11), [0,1,0,1])
    def test4(self):
        self.assertEqual(coins(7), [0,0,1,2])
    def test5(self):
        self.assertEqual(coins(99), [3,2,0,4])
    def test6(self):
        self.assertEqual(coins(105), [4,0,1,0])


class factorial_FuncTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(factorial_Func(5), 120)
    def test1(self):
        self.assertEqual(factorial_Func(7), 5040)
    def test1(self):
        self.assertEqual(factorial_Func(41), 33452526613163807108170062053440751665152000000000)
    def test1(self):
        self.assertEqual(factorial_Func(15), 1307674368000)



    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main() # this runs our tests