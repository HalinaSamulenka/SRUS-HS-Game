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

    def insert_last(self, player):
        """
        insert item at the tail of the list
        :param player:
        :return:
        """
        new_node = PlayerNode(player)  # Create new node
        new_node.prev_node = self.tail_node
        if self.tail_node is None:
            """
            If the list is empty, make new node both head and tail
            """
            self.head_node = new_node
            self.tail_node = new_node
            new_node.next_node = None
        else:
            """
            If the list is not empty, change pointers accordingly,
            new node becomes the new tail
            """
            self.tail_node.next_node = new_node
            new_node.next_node = None
            self.tail_node = new_node
        return new_node

    def delete_first(self):
        """
        Delete an item from the head of the list
        :return:
        """
        if self.head_node is None:
            print("The list has no element to delete")
            return
        if self.head_node.next_node is None:
            self.head_node = None
            return
        self.head_node = self.head_node.next_node
        self.head_node.prev_node = None

    def delete_last(self):
        """
        Delete an item from the tail of the list
        :return:
        """
        if self.tail_node is None:
            print("The list has no element to delete")
            return
        if self.tail_node.prev_node is None:
            self.tail_node = None
            return
        current = self.tail_node
        current.prev_node.next_node = None
        self.tail_node = current.prev_node
        current.prev_node = None






