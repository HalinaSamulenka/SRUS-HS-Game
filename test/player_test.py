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
        # Function that runs before each test to set up
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

    def test_add_password(self):
        """
        test method add_password
        """
        self.player.add_password("test_password")
        assert self.player.verify_password("test_password")

    def test_verify_password(self):
        """
        test verify_password_method
        :return:
        """
        self.player.add_password("test_verify_password")
        assert not self.player.verify_password("verify_password")

    def test_eq_method(self):
        """
        test _eq_ method
        :return:
        """
        expected = self.player.__eq__(10)
        actual = self.player.__eq__(10)
        self.assertEqual(expected, actual)

    def test_ge_method(self):
        """
        test _ge_ method
        :return:
        """
        self.player.set_score(5)
        assert self.player.__ge__(4)

    def test_insertion_sort(self):
        """
        test insertion sort functionality

        """
        player = [Player("1", "Fred"), Player("2", "Aaron"), Player(
            "3", "Jon"), Player("4", "Bob"), Player("5", "Alex")]
        player[0].score = 30
        player[1].score = 78
        player[2].score = 45
        player[3].score = 23
        player[4].score = 1
        Player.insertion_sort(player)
        self.assertEqual(player[0].uid, "2")
        self.assertEqual(player[1].uid, "3")
        self.assertEqual(player[2].uid, "1")
        self.assertEqual(player[3].uid, "4")
        self.assertEqual(player[4].uid, "5")




if __name__== '__name__':
    unittest.main()
