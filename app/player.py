# Create Player class
#
# Filename: player.py
# Project: SRUS-HS-Games
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 11/2/22
# ----------------------------------------------------------------------
import argon2
from argon2 import PasswordHasher


class Player:
    """
    Player class
    """

    def __init__(self, id, name):
        """
        Player constructor
        :param id: string
        :param name: string
        """

        self._id = id
        self._name = name
        self._plaintext_password = None
        self._score = 1

    @property
    def uid(self):
        """
        User ID property
        :return: string
        """
        return self._id

    @property
    def name(self):
        """
        Player`s name property
        :return: string
        """
        return self._name

    def __str__(self):
        """
        String magic staticmethod
        Constructs a human readable form of the instance
        :return: string
        """
        return f"{self.name} ({self.uid})"

    def add_password(self, plaintext_password):
        """
        Add password to Player class
        :param  plaintext_password
        :return:
        """
        ph = PasswordHasher()
        self._plaintext_password = ph.hash(
            plaintext_password)

    def verify_password(self, plaintext_password):
        """
        Verify password to the Player class
        :param plaintext_password:
        :return:
        """
        try:
            return PasswordHasher().verify(self._plaintext_password,
                                           plaintext_password)
        except Exception:
            return False

    def get_score(self):
        """
        implement getter(properties)
        :return: score
        """
        return self.score

    def set_score(self, new_score):
        """
        implement setter for this class
        :param new_score:
        :return:
        """
        self.score = new_score

    def __eq__(self, other):
        """
        implement the __eq__ method in the Player class
        :param other:
        :return:
        """
        if isinstance(other, Player):
            return self.score == other.score
        return False

    def __ge__(self, other):
        """
        implement larger than or equals method
        :param other:
        :return:
        """
        return self.score >= other

    @staticmethod
    def insertion_sort(player):
        """
        implementation insertion sort
        :param player:
        :return: list player
        """
        for i in range(1, len(player)):
            # Set key:
            key = player[i]
            j = i - 1
            while j >= 0 and player[j].score < key.score:
                # Swap:
                player[j + 1] = player[j]
                player[j] = key
                # Decrement 'j':rentposition - 1
                j -= 1


















