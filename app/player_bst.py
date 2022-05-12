# Create the Binary Search Tree class
#
# Filename: player_bst.py
# Project: SRUS-HS-Game
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 21/4/22
# ---------------------------------------------------------------------

from app import player
from app.player_bnode import PlayerBNode

import sys
import math


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

    @root.setter
    def root(self, value):
        self._root = value

    def insert_iterative(self, player):
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

    def insert_recursively(self, player):
        """
        insert recursively Player object (player) into BST
        :param player : object
        """
        if self.root is None:
            # if list is empty, set root to new node
            self.root = PlayerBNode(player)
        else:
            # call the function to insert BST
            self._insert_recursively(player, self.root)

    def _insert_recursively(self, player, current_node):
        """
        insert recursively Player object (player) into BST
        :param player: object
        :param current_node:
        """
        # If player's name is less than current's name
        if player.name < current_node.player.name:
            # If left child node is empty
            if current_node.left_node is None:
                # set child to None
                current_node.left_node = PlayerBNode(player)
            else:
                # to call function passing left node as a current node
                self._insert_recursively(player, current_node.left_node)
        # If player's name is greater than current's name
        if player.name > current_node.player.name:
            # If right child node is empty
            if current_node.right_node is None:
                # set child to None
                current_node.right_node = PlayerBNode(player)
            else:
                # to call function passing right node as a current node
                self._insert_recursively(player, current_node.left_node)

    def search(self, name):
        """
        search player in BST using key (name)
        :param name: of player
        """
        if self.root is not None:
            # if root not equal None to call recursive private function
            return self._search(name, self.root)
        else:
            return None

    def _search(self, name, current_node):
        """
        private search recursive function
        :param name: of player
        :param current_node:
        """
        if name == current_node.player.name:
            # If the root node`s key matches the search name return it
            return current_node.player
        # If the name is less than the root name, search the left
        # subtree
        elif name < current_node.player.name and \
                current_node.left_node != None:
            return self._search(name, current_node.left_node)
        # If the name is greater than the root name, search the right
        # subtree
        elif name > current_node.player.name and \
                current_node.right_node != None:
            return self._search(name, current_node.right_node)

    def create_sorted_list(self, root, nodes):
        """
        This function traverse the skewed binary tree and stores its
        nodes pointers in vector nodes[]
        :param root:
        :param nodes:
        """
        if self.root is None:
            return
        # Store nodes in Inorder (which is sorted order for BST)
        self.create_sorted_list(root.left_node, nodes)
        nodes.append(root)
        self.create_sorted_list(root.right_node, nodes)

    def recursive_construct_bst(self, nodes, start, end):
        """
        Recursive function to construct binary tree
        :param nodes:
        :param start:
        :param end:
        :return: node
        """
        if start > end:
            return None
        # Get the middle element and make it root
        mid = (start + end)//2
        node = nodes[mid]
        # construct left and right subtrees
        node.left_node = self.recursive_construct_bst(nodes, start,mid-1)
        node.right_node = self.recursive_construct_bst(nodes,
                                                       mid + 1, end)
        return node

    def convert_bst_to_balanced_bst(self, root):
        """
        # This functions converts an unbalanced BST to a balanced BST
        :param root:
        """
        # Store nodes of given BST in sorted order
        nodes = []
        self.create_sorted_list(root, nodes)
        # Constructs BST from nodes[]
        n = len(nodes)
        return self.recursive_construct_bst(nodes, 0, n-1)


