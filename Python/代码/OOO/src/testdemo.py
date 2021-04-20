import sys
import unittest
import FileOperation as xml

print(sys.path)
class TestDemo(unittest.TestCase):
    """测试FileOperation.py"""

    @classmethod
    def setUpClass(cls):
        print ("this setupclass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        print ("this teardownclass() method only called once too.\n")

    def setUp(self):
        print ("do something before test : prepare environment.\n")

    def tearDown(self):
        print ("do something after test : clean up.\n")

    def test_openXmlFile(self):
        test = xml.XmlFile()
        print(type(test.openXmlFile))    

if __name__ == "__main__":
    unittest.main(verbosity=2)
    test = xml.XmlFile()
    print(type(test.openXmlFile))