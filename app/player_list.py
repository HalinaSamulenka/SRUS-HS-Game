# Create the class that will implement the double linked list
#
# Filename: player_list.py
# Project: SRUS-HS-Game
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 15/2/22
# ----------------------------------------------------------------------
from app.player_node import PlayerNode


class PlayerList:
    """
    PlayerList class
    """
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert_first(self, player):
        """
        adding a new node at the head of the list
        :param player:
        :return:
        """
        new_node = PlayerNode(player)
        new_node.next_node = self.head_node  # Create new node
        if self.head_node is not None:
            """
            If the list is not empty new node becomes the new head
            """
            self.head_node.prev_node = new_node
            self.head_node = new_node
            new_node.prev_node = None
        else:
            """
            If the list is empty, make new node both head and tail
            """
            self.head_node = new_node
            self.tail_node = new_node
            new_node.prev_node = None
        return new_node
