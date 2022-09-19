import unittest

#getting started with unittesting as a sidebar
def hasMiddleName(name):
    splitName = name.split('')
    return splitName.length == 3


class TestMethods(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()