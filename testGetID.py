import unittest
import sys
from ModifyAlumno import ModifyAlumno
from PySide6.QtWidgets import QApplication
class testGetID(unittest.TestCase):
    app = QApplication(sys.argv)
    modify = ModifyAlumno()
    
    def test_getID(self):
        print(self.modify.getID("1-asdf"))
        self.assertEqual(self.modify.getID("1-test"),"1")
        self.assertNotEqual(self.modify.getID("1:test"),"1")
        self.assertEqual(self.modify.getID("24124122-test"),"24124122")
if __name__ == "__main__":
    unittest.main()