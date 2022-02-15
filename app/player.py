# Title of Application/Code/Class
#
# Short Description if required (delete if not)
#
# Filename: player.py
# Project: SRUS-HS-Games
# Author: Halina Samulenka <20031748@tafe.wa.edu.au>
# Date Created: 11/2/22
# ----------------------------------------------------------------------

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





