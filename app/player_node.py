# Create Player Node
#
# Filename: player_node.py
# Project: SRUS-HS-Game
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 15/2/22
# ----------------------------------------------------------------------
from app.player import Player

class PlayerNode:
    """
    add an initialiser method
    """
    def __init__(self, player):
        self.player = player
        self.next_node = None
        self.prev_node = None

    def get_next_node(self):
        """
        implement getter(properties)
        :return: next node
        """
        return self.next_node

    def get_prev_node(self):
        """
        implement getter(properties)
        :return: previous node
        """
        return self.prev_node

    def get_player(self):
        """
        implement getter(properties)
        :return: player
        """
        return self.player

    def set_player(self, new_player):
        """
        implement setter for this class
        :param new_player:
        :return:
        """
        self.player = new_player

    def set_next(self, new_next):
        """
        implement setter for this class
        :param new_next:
        :return:
        """
        self.next_node = new_next

    def set_prev(self, new_prev):
        """
        implement setter for this class
        :param new_prev:
        :return:
        """
        self.prev_node = new_prev

    @property
    def key(self):
        """
        User key property
        :return: string
        """
        return self.player.uid

    def __str__(self):
        return f"{self.player}"


