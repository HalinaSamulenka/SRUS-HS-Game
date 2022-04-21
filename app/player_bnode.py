# Create PlayerBNode class
#
# Filename: player_bnode.py
# Project: SRUS-HS-Game
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 21/4/22
# ---------------------------------------------------------------------

class PlayerBNode:

    """
    create an initializer method
    """
    def __init__(self, player):
        self.player = player
        self.left_node = None
        self.right_node = None

    def get_left_node(self):
        """
        implement getter(properties)
        :return: left node
        """
        return self.left_node

    def get_right_node(self):
        """
        implement getter(properties)
        :return: right node
        """
        return self.right_node

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

    def set_left(self, new_left):
        """
        implement setter for this class
        :param new_left:
        :return:
        """
        self.left_node = new_left

    def set_right(self, new_right):
        """
        implement setter for this class
        :param new_right:
        :return:
        """
        self.right_node = new_right
