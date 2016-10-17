import sys

from player import Player
from controller import controller_factory

pt1, pt2 = sys.argv[1], sys.argv[2]

p1, p2 = Player("P1"), Player("P2")
p1_handler, p2_handler = controller_factory(1, p1, p2, pt1), controller_factory(2, p2, p1, pt2)

while True:
    p1_handler.play()
    p2_handler.play()
