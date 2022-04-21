# Test the PlayerList class
#
# Filename: player_list_test.py
# Project: SRUS-HS-Game
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 17/2/22
# ----------------------------------------------------------------------
import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class MyPlayerListTestCase(unittest.TestCase):

    def setUp(self):
        #Function that runs before each test to set up
        # pre-requisites
        self.linked_list = PlayerList()

    def test_is_empty(self):
        """
        test empty list
        :return:
        """
        self.assertEqual(self.linked_list.head_node, None)
        self.assertEqual(self.linked_list.tail_node, None)

    def test_insert_first(self):
        """
        insert first node
        :return:
        """
        player = Player("1", "Fred")
        node1 = self.linked_list.insert_first(player)
        self.assertEqual(self.linked_list.head_node, node1)

    def test_insert_last(self):
        """
        insert last node
        :return:
        """
        player = Player("2", "John")
        node2 = self.linked_list.insert_last(player)
        self.assertEqual(self.linked_list.tail_node, node2)

    def test_delete_first(self):
        """
        delete first item
        :return:
        """
        player = Player("3", "Alex")
        node3 = self.linked_list.insert_first(player)
        self.assertEqual(self.linked_list.delete_first(), None)

    def test_delete_first_empty_list(self):
        """
        delete first item if the list is empty
        :return:
        """
        self.assertEqual(self.linked_list.delete_first(), None)

    def test_delete_last(self):
        """
        delete last item
        :return:
        """
        player = Player("3", "Alex")
        node3 = self.linked_list.insert_first(player)
        node4 = self.linked_list.insert_last(player)
        self.assertEqual(self.linked_list.delete_last(), None)

    def test_delete_last_empty_list(self):
        """
        delete last item if the list is empty
        :return:
        """
        self.assertEqual(self.linked_list.delete_last(), None)

    def test_delete_item_based_on_key(self):
        """
        Delete an item from the linked list based on its key
        :return:
        """
        player1 = Player("4", "Alex")
        player2 = Player("5", "Michael")
        node3 = self.linked_list.insert_first(player1)
        node4 = self.linked_list.insert_last(player2)
        self.assertEqual(self.linked_list.delete_item_based_on_key(
            "5"), None)
        self.assertEqual(self.linked_list.delete_item_based_on_key(
            "4"), None)

    def test_display_forward_false(self):
        player1 = Player("1", "Aaron")
        player2 = Player("2", "Fred")
        node = self.linked_list.insert_first(player1)
        node = self.linked_list.insert_last(player2)
        self.linked_list.display_list(forward=False)

    def test_display_forward(self):
        player1 = Player("1", "Aaron")
        player2 = Player("2", "Fred")
        node = self.linked_list.insert_first(player1)
        node = self.linked_list.insert_last(player2)
        self.linked_list.display_list()

    def test_display_empty_list(self):
        self.linked_list.display_list()


if __name__== '__name__':
    unittest.main()