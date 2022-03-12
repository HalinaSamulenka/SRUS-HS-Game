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











