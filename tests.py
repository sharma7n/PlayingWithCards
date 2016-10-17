import unittest

import player
import controller

class ControllerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.player = player.Player('test')
    
    def test_start_turn(self):
        pass
    
    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
