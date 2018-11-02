import unittest
import to_binary


class TestBinary(unittest.TestCase):
    
    def test_zero(self):
        self.assertEquals(binary.to_binary(0),'0')



if __name__=='main':
    unittest.main()    
    