# Create the Binary Search Tree class
#
# Filename: player_bst.py
# Project: SRUS-HS-Game
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 21/4/22
# ---------------------------------------------------------------------
from app.player_bnode import PlayerBNode


class PlayerBST:

    """
    create an initializer method
    """
    def __init__(self):
        self._root = None

    @property
    def root(self):
        """
        PlayerBST root node property
        :return: root node
        """
        return self._root

    def insert(self, player):
        """
        insert Player object (player) into BST
        :param player : object
        """
        new_node = PlayerBNode(player)  # create new node
        if self.root is None:  # if list is empty, set root to new node
            self._root = new_node
        else:
            current = self.root
            while True:
                parent = current
                if player.name < current.player.name:
                    # if player`s name is less that current name
                    current = current.left_node
                    if current is None:
                        parent.left_node = new_node
                        return
                elif player.name > current.player.name:
                    # if player`s name is greater that current name
                    current = current.right_node
                    if current is None:
                        parent.right_node = new_node
                        return

    def search(self, name):
        """
        search player in BST
        :param name of player
        :return: player object
        """
        current = self._root
        # loop while root not match name
        while current.player.name != name:
            # if name is less root`s name search left
            if name < current.player.name:
                current = current.left_node
            else:
                # if name is greater root`s name search left
                current = current.right_node
            if current is None:
                return None
        return current
