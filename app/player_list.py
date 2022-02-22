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

    def is_empty(self):
        """
        the list is empty
        :return: head_node
        """
        return self.head_node == None

    def insert_first(self, player):
        """
        insert a new node if list is not empty
        :param player: string
        :return: new_node
        """
        new_node = PlayerNode(player)
        if self.head_node:
            self.head_node.set_prev(new_node)
        new_node.set_next(self.head_node)
        self.head_node = new_node
        return new_node

