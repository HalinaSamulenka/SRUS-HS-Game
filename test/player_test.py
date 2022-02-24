# Test the Player class
#
# Filename: player_test.py
# Project: SRUS-HS-Games
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 13/2/22
# ----------------------------------------------------------------------
import unittest
from app.player import Player


class MyPlayerTestCase(unittest.TestCase):

    def setUp(self):
        #Function that runs before each test to set up
        # pre-requisites
        self.player = Player("1", "Fred")

    def test_create_player(self):
        #player = Player("1","Fred")
        self.assertIsInstance(self.player, Player)


    def test_string_player(self):
        player = Player("1", "Fred")
        player_string = f"{player}"
        self.assertEqual(player_string, "Fred (1)")

    def test_name_property(self):
        name = self.player.name
        self.assertIsInstance(name, str)
        self.assertEqual(name, "Fred")

    def test_uid_property(self):
       user_id = self.player.uid
       self.assertIsInstance(user_id, str)
       self.assertEqual(user_id, "1")




if __name__== '__name__':
    unittest.main()
