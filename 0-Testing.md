# Unit Testing in Python
**Explore:** [Home](/README.md) [Basics](/0-Basics.md)

## Cheatsheet



### Example
```python
# project/calculator_test.py

import unittest
from code.my_calculator import Calculator

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        calculator = Calculator(8, 2)
        self.assertEqual(calculator.get_sum(), 10, 'The sum is wrong.')

if __name__ == '__main__':
    unittest.main()
```

## Resources
- [unittest | Python3 Libs](https://docs.python.org/3/library/unittest.html#organizing-test-code)
- [Unit Testing | Dataquest.io](https://www.dataquest.io/blog/unit-tests-python/)
- [Python Testing | RealPython](https://realpython.com/python-testing/)
