import unittest
from app import fibonacci, factorial

class TestFibonacci(unittest. TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 89)

    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(30), 1346269)


class TestFactorial(unittest. TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)


# if __name__ == '__main__':
#     unittest.main()

# install pytest with $ pip install pytest
# run test using pytest
# install coverage with $ pip install coverage
# run 
# $ coverage run app.py  #analyses file
# $ coverage report -m    #outputs anaylsys and shows un covered lines
# $ coverage html           # create a more concise html version of the report
# I try out a few things and get 10% code coverage
# I then install pytest-cov using
# $ pip install pytest-cov
# I then run 
# $ pytest --cov=app
# and modify the test_app.py file until I get 100% code coverage
# I also generate a html version of the report using
# $ pytest --cov=app --cov-report=html