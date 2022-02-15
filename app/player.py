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
    # constructor
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

    # getting the values
    def getter1(self):
        return self._uid

    def getter2(self):
        return self._name

    # setting the values
    def setter1(self, uid):
        self._uid = uid

    def setter2(self, name):
        self._name = name

    # deleting the values
    def deleter1(self):
        del self._uid

    def deleter2(self):
        del self._name

    # create a properties
    uid = property(getter1, setter1, deleter1)
    name = property(getter2, setter2, deleter2)

    def __str__(self):
        return f'Player({self.uid}, {self.name})'





